from playwright.sync_api import expect

def validar_todos(comparacoes):
    """
    Valida que os três valores de cada comparação são iguais e não vazios.
    """
    for nome, v1, v2, v3 in comparacoes:
        assert v1, f"{nome} está vazio (primeiro valor)."
        assert v2, f"{nome} está vazio (segundo valor)."
        assert v3, f"{nome} está vazio (span)."
        assert v1 == v2 == v3, (
            f"{nome} divergente:\n"
            f"- Receitas/Despesas: {v1}\n"
            f"- Fluxo de Caixa: {v2}\n"
            f"- Resumo Financeiro: {v3}"
        )
