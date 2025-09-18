import pytest
from playwright.sync_api import expect

#Teste para abrir o button do calendário, alternar entre Período, Mensal e Anual, e selecionar Competência ou Caixa
@pytest.mark.data
def test_filtro_data(page):
    #Clica no Botão Calendário
    page.click("._iconButton_b434_28")

    #Seleciona Mensal
    page.select_option("._select_b434_91", "monthly")

    #Seleciona Anual
    page.select_option("._select_b434_91", "year")

    #Seleciona Período
    page.select_option("._select_b434_91", "period")

    #Seleciona Competência
    page.click("//*[@value='competencia']")

    #Clica em Cancelar
    page.click("._cancelButton_b434_213")

    #Assert para verificar se o botão Cancelar é clicado
    btn = page.locator("//*[@class='ant-btn-icon']").first
    expect(btn).to_be_visible()

"""
como rodar o teste no terminal, para visualizar em arquivo html com Live Server:
pytest -m data --html=report.html --self-contained-html

"""