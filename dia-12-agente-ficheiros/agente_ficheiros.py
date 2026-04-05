import anthropic
import os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

PASTA_BASE = "dia-12-agente-ficheiros/ficheiros"
os.makedirs(PASTA_BASE, exist_ok=True)

# --- Tools reais ---

def list_files() -> str:
    ficheiros = os.listdir(PASTA_BASE)
    if not ficheiros:
        return "Pasta vazia"
    return "\n".join(ficheiros)

def read_file(filename: str) -> str:
    path = os.path.join(PASTA_BASE, filename)
    if not os.path.exists(path):
        return f"Ficheiro '{filename}' não encontrado"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(filename: str, content: str) -> str:
    path = os.path.join(PASTA_BASE, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Ficheiro '{filename}' guardado com sucesso"

# --- Definição das tools ---

tools = [
    {
        "name": "list_files",
        "description": "Lista todos os ficheiros na pasta de trabalho",
        "input_schema": {"type": "object", "properties": {}}
    },
    {
        "name": "read_file",
        "description": "Le o conteudo de um ficheiro",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {"type": "string", "description": "Nome do ficheiro a ler"}
            },
            "required": ["filename"]
        }
    },
    {
        "name": "write_file",
        "description": "Escreve conteudo num ficheiro",
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {"type": "string", "description": "Nome do ficheiro"},
                "content": {"type": "string", "description": "Conteudo a escrever"}
            },
            "required": ["filename", "content"]
        }
    }
]

# --- Loop agentic ---

def executar_agente(tarefa: str):
    print(f"\nTarefa: {tarefa}")
    print("-" * 40)
    messages = [{"role": "user", "content": tarefa}]

    while True:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2048,
            tools=tools,
            messages=messages
        )

        if response.stop_reason == "tool_use":
            messages.append({"role": "assistant", "content": response.content})
            tool_results = []

            for block in response.content:
                if block.type == "tool_use":
                    print(f"  Tool: {block.name}({block.input})")

                    if block.name == "list_files":
                        resultado = list_files()
                    elif block.name == "read_file":
                        resultado = read_file(block.input["filename"])
                    elif block.name == "write_file":
                        resultado = write_file(block.input["filename"], block.input["content"])
                    else:
                        resultado = "Tool nao encontrada"

                    print(f"  Resultado: {resultado[:80]}...")
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": resultado
                    })

            messages.append({"role": "user", "content": tool_results})

        elif response.stop_reason == "end_turn":
            resposta_final = next((b for b in response.content if b.type == "text"), None)
            if resposta_final:
                print(f"\nAgente: {resposta_final.text}")
            break

if __name__ == "__main__":
    # Cria alguns ficheiros de teste
    write_file("notas.txt", "Reuniao amanha as 10h com o cliente.\nLembrar de preparar apresentacao.")
    write_file("compras.txt", "Leite\nPao\nOvos\nQueijo")
    write_file("ideias.txt", "Projeto de app de receitas\nBlog sobre viagens\nCurso de fotografia")

    # Testa o agente
    executar_agente("Le o ficheiro notas.txt e faz um resumo")
    executar_agente("Lista os ficheiros e cria um novo chamado resumo.txt com um indice do que existe em cada ficheiro")