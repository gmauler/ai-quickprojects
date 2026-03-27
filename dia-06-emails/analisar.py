import anthropic
from dotenv import load_dotenv
import os
import sys
import json

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def analisar_email(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        email = f.read()

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"""Analisa este email e responde APENAS com um JSON valido neste formato, sem texto adicional, sem markdown:
{{
  "categoria": "urgente ou informativo ou spam",
  "prioridade": "alta ou media ou baixa",
  "resumo": "uma frase resumindo o email",
  "acao_recomendada": "o que fazer com este email"
}}

Email:
{email}"""
        }]
    )

    resultado = response.content[0].text.strip()

    if resultado.startswith("```"):
        resultado = resultado.split("```")[1]
        if resultado.startswith("json"):
            resultado = resultado[4:]

    print("Raw response:", resultado)
    return json.loads(resultado)

if __name__ == "__main__":
    caminho = sys.argv[1] if len(sys.argv) > 1 else "dia-06-emails/email.txt"
    resultado = analisar_email(caminho)
    print(json.dumps(resultado, indent=2, ensure_ascii=False))