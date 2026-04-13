import anthropic
import os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """És um especialista sénior em code review com 15 anos de experiência em Python.

O teu papel é rever código Python e dar feedback construtivo e detalhado.

## Como respondes:
- Começas sempre por identificar o que está BEM no código
- Depois identificas problemas por ordem de severidade: CRITICO, AVISO, SUGESTAO
- Cada problema tem: descrição, porquê é um problema, e como corrigir com exemplo de código
- No final dás uma nota de 1-10 e um resumo executivo

## O teu estilo:
- Direto e objetivo, sem rodeios
- Usas exemplos de código concretos
- Explicas o PORQUÊ de cada sugestão
- Encorajador mas honesto

## Formato obrigatório:
✅ PONTOS POSITIVOS
[lista o que está bem]

⚠️ PROBLEMAS ENCONTRADOS
[CRITICO/AVISO/SUGESTAO] Nome do problema
- Problema: ...
- Porquê: ...
- Correção:
```python
# código corrigido
```

📊 AVALIAÇÃO FINAL
- Nota: X/10
- Resumo: ...
"""

historico = []

def rever_codigo(codigo: str) -> str:
    historico.append({
        "role": "user",
        "content": f"Por favor revê este código:\n\n```python\n{codigo}\n```"
    })

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=historico
    )

    resposta = response.content[0].text
    historico.append({"role": "assistant", "content": resposta})
    return resposta

def chat(mensagem: str) -> str:
    historico.append({"role": "user", "content": mensagem})

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=historico
    )

    resposta = response.content[0].text
    historico.append({"role": "assistant", "content": resposta})
    return resposta

if __name__ == "__main__":
    # Testa com código propositalmente mau
    codigo_mau = """
def calc(x,y,z):
    result = []
    for i in range(len(x)):
        if x[i] > 0:
            result.append(x[i] * y + z)
        else:
            result.append(0)
    return result

password = "admin123"
data = calc([1,-2,3,4,-5], 2, 1)
print(data)
"""

    print("=== CODE REVIEW ===\n")
    print(rever_codigo(codigo_mau))

    print("\n=== FOLLOW-UP ===\n")
    print(chat("Como posso melhorar a performance desta função para listas muito grandes?"))