from pathlib import Path
import zipfile

# Caminho da raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Pasta onde estão os arquivos ZIP
INPUT_DIR = BASE_DIR / "dados_compactos"

# Pasta onde os arquivos serão extraídos
OUTPUT_DIR = BASE_DIR / "data" / "extracted"


def extract_zip_files():
    """
    Extrai todos os arquivos ZIP da pasta dados_compactos
    organizando os arquivos por ano.
    """

    zip_files = list(INPUT_DIR.rglob("*.zip"))

    if not zip_files:
        print("Nenhum arquivo ZIP encontrado.")
        return

    print(f"Foram encontrados {len(zip_files)} arquivos ZIP.\n")

    for zip_file in zip_files:

        # Descobre o ano através da pasta onde o ZIP está
        ano = zip_file.parent.name

        # Cria a pasta de destino
        output_folder = OUTPUT_DIR / ano
        output_folder.mkdir(parents=True, exist_ok=True)

        print(f"Extraindo: {zip_file.name}")
        print(f"Ano: {ano}")
        print(f"Destino: {output_folder}")

        with zipfile.ZipFile(zip_file, "r") as zip_ref:
            zip_ref.extractall(output_folder)

        print("✓ Extraído com sucesso!\n")

    print("=" * 40)
    print("Extração finalizada com sucesso!")
    print(f"Arquivos processados: {len(zip_files)}")
    print(f"Destino final: {OUTPUT_DIR}")
    print("=" * 40)


extract_zip_files()

