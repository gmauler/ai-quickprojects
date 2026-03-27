import anthropic
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

print("KEY encontrada:", bool(os.getenv("ANTHROPIC_API_KEY")))
print("Caminho .env:", os.path.join(os.path.dirname(__file__), ".env"))
print("Ficheiro existe:", os.path.exists(os.path.join(os.path.dirname(__file__), ".env")))

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

historico = []

print("🤖 Claude Bot — escreve /sair para terminar, /limpar para resetar")
print("-" * 50)

while True:
    user_input = input("\nTu: ").strip()

    if user_input == "/sair":
        print("Até logo!")
        break

    if user_input == "/limpar":
        historico = []
        print("Histórico limpo!")
        continue

    if not user_input:
        continue

    historico.append({
        "role": "user",
        "content": user_input
    })

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=historico
    )

    resposta = response.content[0].text

    historico.append({
        "role": "assistant",
        "content": resposta
    })

    print(f"\nClaude: {resposta}")