from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent

PARQUET = BASE_DIR / "data" / "parquet" / "finbra_consolidado.parquet"

df = pd.read_parquet(PARQUET)

def formatar_moeda(valor):

    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def mostrar_dashboard(df):

    print("=" * 60)
    print("        DESAFIO ANALISTA DE DADOS - SEFAZ")
    print("=" * 60)

    print(f"\nRegistros........: {len(df):,}")

    print(f"Colunas..........: {len(df.columns)}")

    print(f"Anos.............: {df['ano'].nunique()}")

    print(f"UFs..............: {df['uf'].nunique()}")

    print("=" * 60)
if __name__ == "__main__":

    mostrar_dashboard(df)

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

def taxa_execucao(df):

    funcoes = df[df["tipo_conta"] == "Função"]

    empenhado = funcoes[
        funcoes["estagio_despesa"] == "Empenhado"
    ]

    pago = funcoes[
        funcoes["estagio_despesa"] == "Pago"
    ]

    empenhado = (
        empenhado
        .groupby("instituição")["valor"]
        .sum()
    )

    pago = (
        pago
        .groupby("instituição")["valor"]
        .sum()
    )

    resultado = pd.concat(
        [empenhado, pago],
        axis=1
    )

    resultado.columns = [
        "Empenhado",
        "Pago"
    ]

    resultado["Execução (%)"] = (
        resultado["Pago"]
        /
        resultado["Empenhado"]
    ) * 100

    resultado["Execução (%)"] = (
        resultado["Execução (%)"]
        .round(2)
    )

    resultado = resultado.sort_values(
        "Execução (%)",
        ascending=False
    )

    return resultado



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

print("\nTaxa de Execução Financeira:\n")

print(taxa_execucao(df))
