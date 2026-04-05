import anthropic
import os
import subprocess

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def obter_commits(n=20):
    resultado = subprocess.run(
        ["git", "log", "--oneline", f"-{n}"],
        capture_output=True,
        text=True
    )
    return resultado.stdout.strip()

def gerar_changelog(commits):
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        messages=[{
            "role": "user",
            "content": f"""Analisa estes commits de git e gera um CHANGELOG.md profissional.
Agrupa em categorias: Features, Fixes, Docs, CI/CD.
Usa formato markdown com emojis. Data de hoje no topo.

Commits:
{commits}"""
        }]
    )
    return response.content[0].text

def main():
    print("A obter commits...")
    commits = obter_commits(20)
    print(f"Commits encontrados:\n{commits}\n")

    print("A gerar changelog com Claude...")
    changelog = gerar_changelog(commits)

    with open("CHANGELOG.md", "w", encoding="utf-8") as f:
        f.write(changelog)

    print("CHANGELOG.md gerado com sucesso!")
    print("\nPreview:")
    print(changelog[:500])

if __name__ == "__main__":
    main()