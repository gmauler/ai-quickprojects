import anthropic
import os
import fitz

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def extrair_texto_pdf(caminho: str) -> list[str]:
    doc = fitz.open(caminho)
    chunks = []
    for pagina in doc:
        texto = pagina.get_text()
        if texto.strip():
            chunks.append(texto.strip())
    return chunks

def encontrar_chunks_relevantes(chunks: list[str], pergunta: str, max_chunks: int = 3) -> str:
    palavras_chave = pergunta.lower().split()
    scored = []
    for chunk in chunks:
        chunk_lower = chunk.lower()
        score = sum(1 for palavra in palavras_chave if palavra in chunk_lower)
        if score > 0:
            scored.append((score, chunk))
    scored.sort(reverse=True)
    relevantes = [chunk for _, chunk in scored[:max_chunks]]
    return "\n\n---\n\n".join(relevantes) if relevantes else "\n\n---\n\n".join(chunks[:max_chunks])

def responder_pergunta(caminho_pdf: str, pergunta: str) -> str:
    print("A extrair texto do PDF...")
    chunks = extrair_texto_pdf(caminho_pdf)
    print(f"Paginas extraidas: {len(chunks)}")

    print("A encontrar contexto relevante...")
    contexto = encontrar_chunks_relevantes(chunks, pergunta)

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Com base no seguinte contexto extraido de um documento, responde a pergunta.
Se a resposta nao estiver no contexto, diz que nao encontraste essa informacao no documento.

Contexto:
{contexto}

Pergunta: {pergunta}"""
        }]
    )
    return response.content[0].text

if __name__ == "__main__":
    pdf_path = "dia-13-rag/documento.pdf"

    if not os.path.exists(pdf_path):
        print(f"Coloca um PDF em {pdf_path} e corre novamente!")
    else:
        perguntas = [
            "Qual e o tema principal do documento?",
            "Que datas ou prazos sao mencionados?",
            "Quais sao os pontos mais importantes?"
        ]

        for pergunta in perguntas:
            print(f"\n{'='*50}")
            print(f"Pergunta: {pergunta}")
            print(f"{'='*50}")
            resposta = responder_pergunta(pdf_path, pergunta)
            print(f"Resposta: {resposta}")