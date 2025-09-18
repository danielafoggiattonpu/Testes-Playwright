from playwright.sync_api import expect
from playwright_utils import validar_todos
import pytest

#Objetivo do teste: Verificar se o FLUXO DE CAIXA abre corretamente, clicando em ENTRADAS e OUTRAS RECEITAS
@pytest.mark.lista
def test_lista(page):
    #Clica em "Lista"
    page.click("//button[.//div[contains(normalize-space(.), 'Lista')]]")

    # Espera automaticamente até o elemento estar visível
    expect(page.locator("xpath=//*[@class='ag-header-cell-text' and text()='Descrição']")).to_be_visible()
    page.wait_for_timeout(3000) 

    #Clica em "Entradas"
    page.locator("span.anticon-right svg").nth(0).click()

    #Clicas em "Outras Receitas"
    expect(page.locator("text=Outras Receitas")).to_be_visible()

    page.locator("//span[contains(@class, 'anticon-right')]").nth(1).click()
    expect(
        page.locator("//*[@class='_planLeafText_1ls0t_19' and text()='10106 - Receita Diversas']")).to_be_visible()
    page.wait_for_timeout(3000)


#Teste PASSOU
"""
como rodar o teste no terminal, para visualizar em arquivo html com Live Server:
pytest -m lista --html=report.html --self-contained-html

"""

#Objetivo do teste: Comparar se os valores (recebido,pago, realizado, a receber/a pagar/a realizar e comprometido) dos 3 tópicos (RECEITAS/DESPESAS == FLUXO DE CAIXA == RESUMOS FINANCEIROS) são iguais: 
@pytest.mark.comparacao
def test_relacao_receitas_fluxocaixa(page, comparacoes_fixture):
    # Captura valores iniciais (receitas e despesas)
    receitas_despesas_index = page.locator("//*[@class='_value_q7biy_25']")
    receitas_recebido = receitas_despesas_index.nth(0).inner_text()
    receitas_receber = receitas_despesas_index.nth(1).inner_text()
    receitas_comprometido = receitas_despesas_index.nth(2).inner_text()

    despesas_pago = receitas_despesas_index.nth(3).inner_text()
    despesas_pagar = receitas_despesas_index.nth(4).inner_text()
    despesas_comprometido = receitas_despesas_index.nth(5).inner_text()

    # Clica em Lista
    page.locator("//button[.//div[contains(normalize-space(.), 'Lista')]]").click()

    # Aguarda coluna "Descrição" ficar visível
    descricao_assert = page.locator("//*[@class='ag-header-cell-text' and text()='Descrição']")
    expect(descricao_assert).to_be_visible()

    # Captura valores realizados/comprometidos
    entradas_realizado = page.locator("//div[@col-id='realizado']").nth(1).inner_text()
    entradas_realizar = page.locator("//*[@col-id='realizar']").nth(1).inner_text()
    entradas_comprometido = page.locator("//*[@col-id='comprometido']").nth(1).inner_text()

    saidas_realizado = page.locator("//div[@col-id='realizado']").nth(2).inner_text()
    saidas_realizar = page.locator("//*[@col-id='realizar']").nth(2).inner_text()
    saidas_comprometido = page.locator("//*[@col-id='comprometido']").nth(2).inner_text()

    # Captura resumo financeiro
    divs_resumo_financeiro = page.locator("div._info_item_ydohh_76")

    span_indice_receitas_recebido = divs_resumo_financeiro.nth(0).locator("span").inner_text().strip()
    assert span_indice_receitas_recebido == "R$ 240.814.508,80", f"Esperado 'R$ 240.814.508,80', mas foi {span_indice_receitas_recebido}"

    span_indice_receitas_receber = divs_resumo_financeiro.nth(1).locator("span").inner_text().strip()
    assert span_indice_receitas_receber == "R$ 145.301.501,60", f"Esperado 'R$ 145.301.501,60', mas foi {span_indice_receitas_receber}"

    span_indice_receitas_comprometido = divs_resumo_financeiro.nth(3).locator("span").inner_text().strip()
    assert span_indice_receitas_comprometido == "R$ 386.116.010,40", f"Esperado 'R$ 386.116.010,40', mas foi {span_indice_receitas_comprometido}"

    span_indice_despesas_recebido = divs_resumo_financeiro.nth(4).locator("span").inner_text().strip()
    assert span_indice_despesas_recebido == "R$ 262.715.569,70", f"Esperado 'R$ 262.715.569,70', mas foi {span_indice_despesas_recebido}"

    span_indice_despesas_receber = divs_resumo_financeiro.nth(5).locator("span").inner_text().strip()
    assert span_indice_despesas_receber == "R$ 80.993.325,80", f"Esperado 'R$ 80.993.325,80', mas foi {span_indice_despesas_receber}"

    span_indice_despesas_comprometido = divs_resumo_financeiro.nth(7).locator("span").inner_text().strip()
    assert span_indice_despesas_comprometido == "R$ 343.708.895,50", f"Esperado 'R$ 343.708.895,50', mas foi {span_indice_despesas_comprometido}"

    # Cria comparações e valida
    comparacoes = comparacoes_fixture(
        receitas_recebido, receitas_receber, receitas_comprometido,
        despesas_pago, despesas_pagar, despesas_comprometido,
        entradas_realizado, entradas_realizar, entradas_comprometido,
        saidas_realizado, saidas_realizar, saidas_comprometido,
        span_indice_receitas_recebido, span_indice_receitas_receber,
        span_indice_receitas_comprometido, span_indice_despesas_recebido,
        span_indice_despesas_receber, span_indice_despesas_comprometido
    )

    validar_todos(comparacoes)


#Teste FALHOU
"""  AssertionError: Receitas Receber divergente:
E           - Receitas/Despesas: R$ 145.301.501,60
E           - Fluxo de Caixa: R$ 206.912.543,65
E           - Resumo Financeiro: R$ 145.301.501,60
 """


"""
como rodar o teste no terminal, para visualizar em arquivo html com Live Server:
pytest -m comparacao --html=report.html --self-contained-html

"""