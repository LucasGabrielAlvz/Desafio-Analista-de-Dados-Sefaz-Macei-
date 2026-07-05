def linha(tamanho=70):
    """Imprime uma linha separadora."""
    print("=" * tamanho)


def titulo(texto):
    """Imprime um título formatado."""
    linha()
    print(texto.center(70))
    linha()


def subtitulo(texto):
    """Imprime um subtítulo."""
    print(f"\n{texto}")
    linha()


def formatar_moeda(valor):
    """Formata valores monetários para o padrão brasileiro."""

    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def formatar_percentual(valor):
    """Formata percentuais."""

    return f"{valor:.2f}%".replace(".", ",")


def destaque(texto):
    """Imprime um destaque."""

    print(f"\n>>> {texto}")


def fim_relatorio():
    """Mensagem final do relatório."""

    linha()

    print("Relatório finalizado com sucesso.".center(70))

    linha()