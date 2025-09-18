from centro_de_custo_data import cenarios, verificar_valores_por_indice
from playwright.sync_api import expect
import pytest

#Objetivo do teste: Clicar em Filtros, selecionar o cenário(nome da Empresa) e obter os valores correspondentes a "receitas_total_recebido",             "receitas_total_a_receber", "receitas_comprometido", "despesas_total_pago", "despesas_total_a_pagar" e "despesas_comprometido"
@pytest.mark.btnfiltro
@pytest.mark.parametrize("opcao, valores", cenarios)
def test_button_dropdown(page, opcao, valores):
    #iníciar a page
    titulo = page.locator("//*[@class='_title_module_6wxw3_19']")
    expect(titulo).to_have_text("Modulo Financeiro")
    
    #clicar no botão 'Filtros'
    page.click("._header_filters_1ygc3_5")

    #Clicar no Dropdown 'Centro de Custo'
    centro_de_custo = page.locator("//h1[text()='Centro de Custo']")
    expect(centro_de_custo).to_be_visible()

    #Clicar no botão 'x' para limpar itens pré-existentes
    remove_itens = page.locator(".ant-select-selection-item-remove")
    count = remove_itens.count()
    for i in range(count):
        remove_itens.nth(i).click()

    #Selecionar a opção 
    page.locator(".ant-select-selection-overflow").nth(2).click()
    page.locator(f"//*[text()='{opcao}']").click()
    #Aplicar Filtros
    page.locator("//span[text()='Aplicar Filtros']").click()

    #Resultado Esperado 
    verificar_valores_por_indice(page, valores) 

#Teste PASSOU
"""
como rodar o teste no terminal, para visualizar em arquivo html com Live Server:
pytest -m btnfiltro --html=report.html --self-contained-html

"""