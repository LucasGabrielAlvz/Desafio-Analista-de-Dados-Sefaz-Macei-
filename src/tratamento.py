from pathlib import Path
import pandas as pd

from leitura import load_csv_files


def process_data():

    # Carrega os DataFrames
    dados = load_csv_files()

    dataframes = []

    # Adiciona a coluna Ano em cada DataFrame
    for ano, df in dados.items():

        df["Ano"] = ano

        dataframes.append(df)

    # Consolida todos os DataFrames
    df_final = pd.concat(
        dataframes,
        ignore_index=True
    )

    # Padronização dos nomes das colunas
    df_final.columns = (
        df_final.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Novas colunas para facilitar as análises
    df_final["tipo_conta"] = "Total"
    df_final["codigo_conta"] = pd.NA
    df_final["nome_conta"] = pd.NA

    # Identificação de Função e Subfunção
    for indice, conta in df_final["conta"].items():

        if " - " in conta:

            codigo, nome = conta.split(" - ", 1)

            if "." in codigo:
                tipo = "Subfunção"
            else:
                tipo = "Função"

            df_final.at[indice, "tipo_conta"] = tipo
            df_final.at[indice, "codigo_conta"] = codigo
            df_final.at[indice, "nome_conta"] = nome

        else:

            df_final.at[indice, "nome_conta"] = conta

    # Padronização do estágio da despesa
    mapa_estagios = {
        "Despesas Empenhadas": "Empenhado",
        "Despesas Liquidadas": "Liquidado",
        "Despesas Pagas": "Pago",
        "Inscrição de Restos a Pagar Não Processados": "RPNP",
        "Inscrição de Restos a Pagar Processados": "RPP"
    }

    df_final["estagio_despesa"] = df_final["coluna"].replace(mapa_estagios)

    # Caminho para salvar o Parquet
    BASE_DIR = Path(__file__).resolve().parent.parent

    OUTPUT_DIR = BASE_DIR / "data" / "parquet"

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Salva o DataFrame consolidado
    df_final.to_parquet(
        OUTPUT_DIR / "finbra_consolidado.parquet",
        index=False
    )

    print("\nArquivo Parquet salvo com sucesso!")

    return df_final


if __name__ == "__main__":

    df = process_data()

    print("\nInformações do DataFrame:")
    print(df.info())

    print("\nDimensões:")
    print(df.shape)

    print("\nPrimeiras linhas:")
    print(df.head())