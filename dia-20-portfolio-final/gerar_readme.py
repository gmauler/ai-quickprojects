import anthropic
import os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

projetos = """
Dia 1: Setup do repositório GitHub com estrutura organizada
Dia 2: Hello World com a API do Claude (Anthropic SDK)
Dia 3: Resumidor de texto via CLI com argparse
Dia 4: GitHub Actions com lint automático usando ruff
Dia 5: Chatbot com histórico de conversa no terminal
Dia 6: Analisador de emails com classificação JSON
Dia 7: Webhook com FastAPI e endpoint /process
Dia 8: Deploy automático no Railway com CI/CD
Dia 9: Gerador de CHANGELOG automático a partir de git log
Dia 10: Automação visual com n8n ligado ao FastAPI
Dia 11: Agente com tool use (weather API real)
Dia 12: Agente que lê, escreve e lista ficheiros
Dia 13: RAG simples para perguntas sobre PDFs
Dia 14: CI/CD com pytest e análise de erros por IA
Dia 15: Agente de research com web search e fontes
Dia 16: Interface web de chat em HTML/JS
Dia 17: Especialista de code review com system prompt
Dia 18: Pipeline de categorização de CSVs com pandas
Dia 19: Documentação automática de funções Python
Dia 20: README de portfólio gerado com IA
"""

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    messages=[{
        "role": "user",
        "content": f"""Cria um README.md profissional e impressionante para um repositório GitHub.

O repositório chama-se "ai-quickprojects" e pertence a Gustavo Mauler.
É um plano de 20 dias de projetos práticos de AI completados com sucesso.

Projetos completados:
{projetos}

Stack usado: Python 3.14, Anthropic API (Claude), FastAPI, GitHub Actions, Railway, n8n, pandas, PyMuPDF

O README deve ter:
- Título e descrição apelativa
- Badge de status (todos completos)
- Secção "O que aprendi" com insights reais
- Tabela de projetos com emoji, nome e tecnologias
- Secção de stack com badges bonitos
- Instruções de como correr localmente
- Secção sobre o autor (Gustavo Mauler, Portugal)

Usa emojis, formatting markdown bonito e um tom profissional mas pessoal.
Este README vai ser visto por recrutadores e outros developers."""
    }]
)

readme = response.content[0].text

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)

print("README.md gerado!")
print("\nPreview das primeiras linhas:")
print("\n".join(readme.split("\n")[:20]))