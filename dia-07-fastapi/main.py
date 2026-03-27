import anthropic
import os
from fastapi import FastAPI
from pydantic import BaseModel

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app = FastAPI()

class Pedido(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process")
def process(pedido: Pedido):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": pedido.text}]
    )
    return {"result": message.content[0].text}