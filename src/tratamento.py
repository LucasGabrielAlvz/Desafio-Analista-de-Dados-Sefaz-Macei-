from pathlib import Path
import pandas as pd

from leitura import load_csv_files


def process_data():

    dados = load_csv_files()

    dataframes = []

    for ano, df in dados.items():

        df["Ano"] = ano

        dataframes.append(df)

    df_final = pd.concat(
        dataframes,
        ignore_index=True
    )

    return df_final


if __name__ == "__main__":

    df = process_data()

    print(df.shape)