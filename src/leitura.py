from pathlib import Path
import pandas as pd

# Caminho da raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Pasta onde estão os CSVs extraídos
INPUT_DIR = BASE_DIR / "data" / "extracted"


def load_csv_files():
    """
    Lê todos os arquivos CSV extraídos e
    armazena cada DataFrame em um dicionário.

    Chave: ano
    Valor: DataFrame
    """

    csv_files = list(INPUT_DIR.rglob("*.csv"))

    if not csv_files:
        print("Nenhum arquivo CSV encontrado.")
        return {}

    dados = {}

    for csv_file in csv_files:

        ano = csv_file.parent.name

        print(f"Lendo dados de {ano}...")

        df = pd.read_csv(
            csv_file,
            sep=";",
            skiprows=3,
            encoding="latin-1",
            decimal=","
        )

        dados[ano] = df

        print(f"✓ {len(df)} linhas carregadas.")

    print("\nLeitura concluída com sucesso!")

    return dados


if __name__ == "__main__":

    dados = load_csv_files()

    print("\nArquivos carregados:")

    for ano in dados:
        print(f"{ano}: {dados[ano].shape}")