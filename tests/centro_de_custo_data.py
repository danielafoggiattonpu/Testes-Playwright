from playwright.sync_api import Page, expect

#Função criada para agrupar os dados dos vários cenários(empresas) utilizados como parâmetro no teste "dropdown_filtros_test"
def verificar_valores_por_indice(page: Page, valores_esperados_dict):
    ordem_chaves = [
        "receitas_total_recebido",
        "receitas_total_a_receber",
        "receitas_comprometido",
        "despesas_total_pago",
        "despesas_total_a_pagar",
        "despesas_comprometido"
    ]

    for i, chave in enumerate(ordem_chaves, start=1):
        valor_esperado = valores_esperados_dict[chave]
        locator = page.locator(f"(//h2[contains(@class, '_value')])[{i}]")
        valor_real = locator.inner_text(timeout=5000).strip()
        try:
            expect(locator).to_contain_text(valor_esperado, timeout=5000)
        except AssertionError:
            raise AssertionError(
                f"❌ Esperado '{valor_esperado}' no elemento {i} ({chave}), mas foi {valor_real}."
            )

cenarios = [
    (
        "1 - Centro de Custo - 1",
        {
            "receitas_total_recebido": "R$ 3.524",
            "receitas_total_a_receber": "R$ 194",
            "receitas_comprometido": "R$ 3.718",
            "despesas_total_pago": "R$ 5.583",
            "despesas_total_a_pagar": "R$ 1.643",
            "despesas_comprometido": "R$ 7.227"
        }
    ),
    (
        "2 - Centro de Custo - 2",
        {
            "receitas_total_recebido": "R$ 0,00",
            "receitas_total_a_receber": "R$ 0,00",
            "receitas_comprometido": "R$ 0,00",
            "despesas_total_pago": "R$ 0,00",
            "despesas_total_a_pagar": "R$ 0,00",
            "despesas_comprometido": "R$ 0,00"
        }
    ),
    (
        "3 - Centro de Custo - 3",
        {
            "receitas_total_recebido": "R$ 2.515",
            "receitas_total_a_receber": "R$ 0,00",
            "receitas_comprometido": "R$ 2.515",
            "despesas_total_pago": "R$ 0,00",
            "despesas_total_a_pagar": "R$ 0,00",
            "despesas_comprometido": "R$ 0,00"
        }
    ),
    (
        "4 - Centro de Custo - 4",
        {
            "receitas_total_recebido": "R$ 0,00",
            "receitas_total_a_receber": "R$ 0,00",
            "receitas_comprometido": "R$ 0,00",
            "despesas_total_pago": "R$ 1.207",
            "despesas_total_a_pagar": "R$ 69.941",
            "despesas_comprometido": "R$ 1.277"
        }
    ),
    (
        "6 - Centro de Custo - 6",
        {
            "receitas_total_recebido": "R$ 0,00",
            "receitas_total_a_receber": "R$ 0,00",
            "receitas_comprometido": "R$ 0,00",
            "despesas_total_pago": "R$ 0,00",
            "despesas_total_a_pagar": "R$ 0,00",
            "despesas_comprometido": "R$ 0,00"
        }
    )
]

