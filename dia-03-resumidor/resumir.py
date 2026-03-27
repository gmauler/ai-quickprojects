from dotenv import load_dotenv
import os
import sys
import anthropic

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def resumir(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        texto = f.read()

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Resume o seguinte texto em 3 pontos claros:\\n\\n{texto}"
        }]
    )
    return message.content[0].text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python resumir.py <ficheiro.txt>")
        sys.exit(1)

    resultado = resumir(sys.argv[1])
    print(resultado)