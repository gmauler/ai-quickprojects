import anthropic
import os
import requests

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

import requests

def get_weather(city: str) -> str:
    api_key = os.getenv("OPENWEATHER_API_KEY")
    print(f"  [debug] API key encontrada: {bool(api_key)}")
    
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "lang": "pt"
    }
    
    response = requests.get(url, params=params)
    print(f"  [debug] Status code: {response.status_code}")
    print(f"  [debug] Resposta: {response.json()}")
    
    if response.status_code != 200:
        return f"Erro ao obter dados para {city}"
    
    data = response.json()
    temp = data["main"]["temp"]
    descricao = data["weather"][0]["description"]
    vento = data["wind"]["speed"]
    humidade = data["main"]["humidity"]
    
    return f"{temp}°C, {descricao}, vento {vento}m/s, humidade {humidade}%"

tools = [
    {
        "name": "get_weather",
        "description": "Obtem o tempo atual de uma cidade",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "O nome da cidade"}
            },
            "required": ["city"]
        }
    }
]

def executar_agente(pergunta: str):
    print(f"\nPergunta: {pergunta}")
    print("-" * 40)
    messages = [{"role": "user", "content": pergunta}]

    while True:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1024,
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"Claude quer usar: {block.name}({block.input})")
                    resultado = get_weather(block.input["city"]) if block.name == "get_weather" else "Tool nao encontrada"
                    print(f"Resultado: {resultado}")
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": resultado
                    })
            messages.append({"role": "user", "content": tool_results})

        elif response.stop_reason == "end_turn":
            resposta_final = next(b for b in response.content if b.type == "text")
            print(f"\nResposta final: {resposta_final.text}")
            break

if __name__ == "__main__":
    print("A iniciar agente...")
    executar_agente("Que tempo esta em Lisboa e no Porto?")
    executar_agente("Devo levar chapeu de chuva se for a Faro amanha?")