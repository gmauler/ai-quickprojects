import anthropic
import os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def fazer_research(pergunta: str):
    print(f"\nPergunta: {pergunta}")
    print("-" * 50)

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search"
        }],
        messages=[{
            "role": "user",
            "content": pergunta
        }]
    )

    fontes = []

    for block in response.content:
        if block.type == "server_tool_use":
            print(f"A pesquisar: {block.input.get('query', '')}")
        elif block.type == "web_search_tool_result":
            # Extrai fontes dos resultados
            if hasattr(block, "content") and block.content:
                for item in block.content:
                    if hasattr(item, "url"):
                        fontes.append({"url": item.url, "titulo": getattr(item, "title", "")})
        elif block.type == "text" and block.text:
            print(f"\nResposta:\n{block.text}")

    if fontes:
        print("\n📚 Fontes:")
        for i, fonte in enumerate(fontes, 1):
            print(f"  {i}. {fonte['titulo']}")
            print(f"     {fonte['url']}")

if __name__ == "__main__":
    fazer_research("Modelos de AI lancados em 2026")