import pytest
from playwright.sync_api import expect

#Objetivo do teste: Em INDICADORES FINANCEIROS, clicar em cada empresa (1 até 5) e fazer assert que o título está displayed.
@pytest.mark.parametrize("xpath_empresa", [
    "//*[text()='1 - Empresa - 1']",
    "//*[text()='2 - Empresa - 2']",
    "//*[text()='3 - Empresa - 3']",
    "//*[text()='4 - Empresa - 4']",
    "//*[text()='5 - Empresa - 5']"
])

@pytest.mark.indicadores
def test_indicadores_financeiros(page, xpath_empresa):
    #Selecionar o TMA
    page.click("#react-select-2-input")
    #Selecionar a opção 0
    page.locator("//*[text()='0']").click()

    #Aplicar
    page.click("//*[@class='_filter_button_6wxw3_214 ' and text()='Aplicar']")
    
    #Clicar na empresa correspondente (1 até 5)
    page.locator(xpath_empresa).click()

    #Aguarda e verifica se o título do empreendimento está visível
    name_business = page.locator("//*[@class='_empreendimento_name_1tmxl_40']")
    expect(name_business).to_be_visible()

    print("✅ Título do empreendimento exibido corretamente.")
    

"""

pytest -m indicadores --html=report.html --self-contained-html

"""