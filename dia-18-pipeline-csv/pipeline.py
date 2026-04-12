import anthropic
import os
import pandas as pd
import json

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def categorizar_lote(transacoes: list) -> list:
    lista = "\n".join([f"{t['id']}. {t['descricao']} ({t['valor']}€)" for t in transacoes])

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"""Categoriza estas transacoes financeiras.
Responde APENAS com JSON valido, sem texto adicional, neste formato exacto:
[
  {{"id": 1, "categoria": "Transporte", "essencial": true, "emoji": "🚗"}},
  ...
]

Categorias possiveis: Transporte, Alimentacao, Entretenimento, Saude, Educacao, Casa, Desporto, Outro

Transacoes:
{lista}"""
        }]
    )

    resultado = response.content[0].text.strip()
    if resultado.startswith("```"):
        resultado = resultado.split("```")[1]
        if resultado.startswith("json"):
            resultado = resultado[4:]

    return json.loads(resultado)

def processar_csv(input_path: str, output_path: str):
    print(f"A ler {input_path}...")
    df = pd.read_csv(input_path)
    print(f"Linhas encontradas: {len(df)}")

    transacoes = df.to_dict("records")

    print("A categorizar com Claude...")
    categorias = categorizar_lote(transacoes)

    cat_dict = {c["id"]: c for c in categorias}

    df["categoria"] = df["id"].map(lambda x: cat_dict.get(x, {}).get("categoria", "Outro"))
    df["essencial"] = df["id"].map(lambda x: cat_dict.get(x, {}).get("essencial", False))
    df["emoji"] = df["id"].map(lambda x: cat_dict.get(x, {}).get("emoji", "❓"))

    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"\nCSV guardado em {output_path}")
    print("\nResultado:")
    print(df.to_string(index=False))

    print("\nResumo por categoria:")
    resumo = df.groupby("categoria")["valor"].agg(["count", "sum"]).round(2)
    resumo.columns = ["transacoes", "total_euros"]
    print(resumo)

if __name__ == "__main__":
    processar_csv(
        "dia-18-pipeline-csv/transacoes.csv",
        "dia-18-pipeline-csv/transacoes_processadas.csv"
    )