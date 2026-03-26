import anthropic
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

print("KEY encontrada:", bool(os.getenv("ANTHROPIC_API_KEY")))

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Explica o que és em 2 frases."}]
)

print(message.content[0].text)