import anthropic
import os
import ast

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def encontrar_funcoes_sem_docstring(caminho: str) -> list:
    with open(caminho, "r", encoding="utf-8") as f:
        codigo = f.read()

    tree = ast.parse(codigo)
    funcoes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            tem_docstring = (
                isinstance(node.body[0], ast.Expr) and
                isinstance(node.body[0].value, ast.Constant)
            )
            if not tem_docstring:
                funcoes.append({
                    "nome": node.name,
                    "linha": node.lineno,
                    "codigo": ast.get_source_segment(codigo, node)
                })

    return funcoes

def gerar_docstring(codigo_funcao: str) -> str:
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=512,
        messages=[{
            "role": "user",
            "content": f"""Gera uma docstring profissional para esta função Python.
Responde APENAS com a docstring, sem codigo adicional, sem aspas triplas.
Inclui: descricao, Args e Returns.

Funcao:
{codigo_funcao}"""
        }]
    )
    return response.content[0].text.strip()

def adicionar_docstrings(caminho: str):
    print(f"\nA analisar: {caminho}")
    funcoes = encontrar_funcoes_sem_docstring(caminho)

    if not funcoes:
        print("Todas as funcoes ja tem docstrings!")
        return

    print(f"Funcoes sem docstring: {len(funcoes)}")

    with open(caminho, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    # Processa de baixo para cima para nao deslocar linhas
    for funcao in sorted(funcoes, key=lambda x: x["linha"], reverse=True):
        print(f"  A documentar: {funcao['nome']}()...")
        docstring = gerar_docstring(funcao["codigo"])

        # Encontra a linha de inserção (depois do def)
        linha_def = funcao["linha"] - 1
        linha_corpo = linha_def + 1

        # Determina a indentacao
        indent = ""
        for char in linhas[linha_corpo]:
            if char in (" ", "\t"):
                indent += char
            else:
                break

        docstring_formatada = f'{indent}"""\n'
        for linha in docstring.split("\n"):
            docstring_formatada += f"{indent}{linha}\n"
        docstring_formatada += f'{indent}"""\n'

        linhas.insert(linha_corpo, docstring_formatada)

    with open(caminho, "w", encoding="utf-8") as f:
        f.writelines(linhas)

    print(f"Docstrings adicionadas com sucesso!")

if __name__ == "__main__":
    ficheiros = [
        "dia-14-ci-testes/calculadora.py",
        "dia-07-fastapi/main.py",
    ]

    for ficheiro in ficheiros:
        if os.path.exists(ficheiro):
            adicionar_docstrings(ficheiro)
        else:
            print(f"Ficheiro nao encontrado: {ficheiro}")

    print("\nConcluido! Verifica os ficheiros no VS Code.")