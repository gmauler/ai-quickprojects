import anthropic
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pedido(BaseModel):
    text: str

@app.get("/health")
def health():
    """
    Verifica o status de saúde da aplicação.
    
    Realiza uma verificação básica para confirmar que a aplicação está operacional
    e responsiva. Utilizado para monitoramento de disponibilidade e testes de
    conectividade.
    
    Args:
        Nenhum.
    
    Returns:
        dict: Dicionário contendo o status da aplicação com a chave 'status'
              definida como 'ok' quando a aplicação está funcionando corretamente.
    """
    return {"status": "ok"}

@app.post("/process")
def process(pedido: Pedido):
    """
    def process(pedido: Pedido) -> dict:
        """
        Processa um pedido utilizando o modelo Claude Haiku para gerar uma resposta.
        
        Envia o texto do pedido para a API do Claude e retorna a resposta gerada pelo modelo
        de inteligência artificial.
        
        Args:
            pedido (Pedido): Objeto contendo os dados do pedido, incluindo o atributo 'text'
                            com o conteúdo a ser processado.
        
        Returns:
            dict: Dicionário contendo a chave 'result' com a resposta gerada pelo modelo Claude.
                  Exemplo: {"result": "texto da resposta gerada"}
        """
    """
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": pedido.text}]
    )
    return {"result": message.content[0].text}