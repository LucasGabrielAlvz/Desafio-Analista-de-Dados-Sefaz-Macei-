from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

PARQUET = BASE_DIR / "data" / "parquet" / "finbra_consolidado.parquet"

df = pd.read_parquet(PARQUET)

def capitais_por_ano(df):

    resultado = (
        df.groupby("ano")["instituição"]
        .nunique()
        .sort_index()
    )

    return resultado
print("\nQuantidade de capitais por ano:\n")

print(capitais_por_ano(df))

def registros_por_ano(df):

    resultado = (
        df.groupby("ano")
        .size()
        .sort_index()
    )

    return resultado
print("\nQuantidade de registros por ano:\n")
print(registros_por_ano(df))

def panorama_estagios(df):

    resultado = (

        df.groupby("estagio_despesa")["valor"]

        .sum()

        .sort_values(ascending=False)

    )

    return resultado
print("\nTotal por estágio da despesa:\n")
print(panorama_estagios(df))

def ranking_saude(df):

    saude = df[

        (df["tipo_conta"] == "Função") &

        (df["nome_conta"] == "Saúde") &

        (df["estagio_despesa"] == "Pago")

    ]

    ranking = (

        saude.groupby("instituição")["valor"]

        .sum()

        .sort_values(ascending=False)

    )

    return ranking
print("\nRanking de gastos pagos em Saúde:\n")
print(ranking_saude(df))

