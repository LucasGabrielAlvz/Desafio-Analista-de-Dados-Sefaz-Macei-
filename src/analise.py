from pathlib import Path

import pandas as pd

from utils import (
    formatar_moeda,
    linha,
    titulo,
    subtitulo,
    formatar_percentual,
    fim_relatorio,
)

BASE_DIR = Path(__file__).resolve().parent.parent
PARQUET = BASE_DIR / "data" / "parquet" / "finbra_consolidado.parquet"


# ======================================================
# Carregamento
# ======================================================

def carregar_dados() -> pd.DataFrame:
    """
    Carrega o arquivo consolidado em formato Parquet.
    """
    return pd.read_parquet(PARQUET)


# ======================================================
# Dashboard
# ======================================================

def mostrar_dashboard(df: pd.DataFrame) -> None:
    """Exibe informações gerais do conjunto de dados."""

    titulo("DESAFIO ANALISTA DE DADOS - SEFAZ")

    print(f"{'Registros':<20}: {len(df):,}".replace(",", "."))
    print(f"{'Colunas':<20}: {len(df.columns)}")
    print(f"{'Anos':<20}: {df['ano'].nunique()}")
    print(f"{'UFs':<20}: {df['uf'].nunique()}")

    linha()


# ======================================================
# Análises
# ======================================================

def capitais_por_ano(df: pd.DataFrame) -> pd.Series:
    """Quantidade de capitais presentes em cada ano."""

    return (
        df.groupby("ano")["instituição"]
        .nunique()
        .sort_index()
    )


def registros_por_ano(df: pd.DataFrame) -> pd.Series:
    """Quantidade de registros por ano."""

    return (
        df.groupby("ano")
        .size()
        .sort_index()
    )


def panorama_estagios(df: pd.DataFrame) -> pd.Series:
    """Total financeiro por estágio da despesa."""

    return (
        df.groupby("estagio_despesa")["valor"]
        .sum()
        .sort_values(ascending=False)
    )


def taxa_execucao(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula a taxa de execução financeira das capitais."""

    funcoes = df[df["tipo_conta"] == "Função"]

    empenhado = (
        funcoes[
            funcoes["estagio_despesa"] == "Empenhado"
        ]
        .groupby("instituição")["valor"]
        .sum()
    )

    pago = (
        funcoes[
            funcoes["estagio_despesa"] == "Pago"
        ]
        .groupby("instituição")["valor"]
        .sum()
    )

    resultado = pd.concat(
        [empenhado, pago],
        axis=1
    )

    resultado.columns = ["Empenhado", "Pago"]

    resultado["Execução (%)"] = (
        resultado["Pago"]
        / resultado["Empenhado"]
        * 100
    ).round(2)

    return resultado.sort_values(
        "Execução (%)",
        ascending=False
    )


def ranking_saude(df: pd.DataFrame) -> pd.Series:
    """Ranking de gastos pagos na função Saúde."""

    saude = df[
        (df["tipo_conta"] == "Função")
        & (df["nome_conta"] == "Saúde")
        & (df["estagio_despesa"] == "Pago")
    ]

    return (
        saude.groupby("instituição")["valor"]
        .sum()
        .sort_values(ascending=False)
    )


# ======================================================
# Impressão
# ======================================================

def imprimir_capitais(df: pd.DataFrame) -> None:

    subtitulo("Quantidade de capitais por ano")

    print(capitais_por_ano(df))


def imprimir_registros(df: pd.DataFrame) -> None:

    subtitulo("Quantidade de registros por ano")

    print(registros_por_ano(df))


def imprimir_estagios(df: pd.DataFrame) -> None:
    """Exibe o total financeiro por estágio da despesa."""

    subtitulo("Panorama dos estágios da despesa")

    resultado = panorama_estagios(df)

    for estagio, valor in resultado.items():
        print(f"{estagio:<15} {formatar_moeda(valor)}")


def imprimir_ranking_saude(df: pd.DataFrame) -> None:
    """Exibe o ranking de gastos pagos em Saúde."""

    subtitulo("Ranking de gastos pagos em Saúde")

    ranking = ranking_saude(df)

    for posicao, (capital, valor) in enumerate(
        ranking.items(),
        start=1
    ):
        print(
            f"{posicao:>2}º "
            f"{capital:<45}"
            f"{formatar_moeda(valor)}"
        )


def imprimir_execucao(df: pd.DataFrame) -> None:

    resultado = taxa_execucao(df)

    subtitulo("TOP 10 - Taxa de Execução Financeira")

    for posicao, (capital, dados) in enumerate(
        resultado.head(10).iterrows(),
        start=1
    ):

        print(
            f"{posicao:>2}º "
            f"{capital:<45}"
            f"{formatar_percentual(dados['Execução (%)'])}"
        )

def indicadores_maceio(df: pd.DataFrame) -> None:
    """
    Exibe indicadores específicos da Prefeitura de Maceió.
    """

    subtitulo("Indicadores - Prefeitura de Maceió")

    maceio = "Prefeitura Municipal de Maceió - AL"

    ranking = ranking_saude(df)

    posicao_saude = ranking.index.get_loc(maceio) + 1

    gasto_saude = ranking.loc[maceio]

    execucao = taxa_execucao(df)

    posicao_execucao = execucao.index.get_loc(maceio) + 1

    percentual = execucao.loc[maceio, "Execução (%)"]

    populacao = (
        df.loc[
            df["instituição"] == maceio,
            "população"
        ]
        .dropna()
        .iloc[0]
    )

    gasto_por_habitante = gasto_saude / populacao

    print(f"Posição em Saúde........: {posicao_saude}º")
    print(f"Gasto em Saúde..........: {formatar_moeda(gasto_saude)}")
    print(f"Execução Financeira.....: {formatar_percentual(percentual)}")
    print(f"Posição em Execução.....: {posicao_execucao}º")
    print(f"População...............: {int(populacao):,}".replace(",", "."))
    print(
        f"Gasto por Habitante.....: "
        f"{formatar_moeda(gasto_por_habitante)}"
    )

def insight_maceio(df: pd.DataFrame) -> None:
    """Resumo interpretativo dos indicadores de Maceió."""

    subtitulo("Insight")

    print(
        "Entre as capitais brasileiras, Maceió apresenta "
        "uma elevada taxa de execução financeira, figurando "
        "entre as dez melhores do país. Apesar de possuir "
        "um volume absoluto de gastos inferior ao das maiores "
        "capitais, mantém um bom desempenho na aplicação dos "
        "recursos públicos destinados à Saúde."
    )


# ======================================================
# Main
# ======================================================

def main() -> None:

    df = carregar_dados()

    mostrar_dashboard(df)

    imprimir_capitais(df)

    imprimir_registros(df)

    imprimir_estagios(df)

    imprimir_ranking_saude(df)

    indicadores_maceio(df)

    insight_maceio(df)

    imprimir_execucao(df)

    fim_relatorio()


if __name__ == "__main__":
    main()