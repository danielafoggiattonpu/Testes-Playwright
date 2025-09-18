from playwright.sync_api import sync_playwright
import os
import pytest
import time

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture
def page(browser):
    link = os.getenv("LINK")
    if not link:
        raise ValueError("A variável LINK não está definida.")
    context = browser.new_context()
    page = context.new_page()
    page.goto(link) 
    yield page
    time.sleep(3)
    context.close()

@pytest.fixture
def comparacoes_fixture():
    def _montar(receitas_recebido, receitas_receber, receitas_comprometido,
                despesas_pago, despesas_pagar, despesas_comprometido,
                entradas_realizado, entradas_realizar, entradas_comprometido,
                saidas_realizado, saidas_realizar, saidas_comprometido,
                span_indice_receitas_recebido, span_indice_receitas_receber,
                span_indice_receitas_comprometido, span_indice_despesas_pago,
                span_indice_despesas_pagar, span_indice_despesas_comprometido):
        return [
            ("Receitas Recebido", receitas_recebido, entradas_realizado, span_indice_receitas_recebido),
            ("Receitas Receber", receitas_receber, entradas_realizar, span_indice_receitas_receber),
            ("Receitas Comprometido", receitas_comprometido, entradas_comprometido, span_indice_receitas_comprometido),
            ("Despesas Pago", despesas_pago, saidas_realizado, span_indice_despesas_pago),
            ("Despesas Pagar", despesas_pagar, saidas_realizar, span_indice_despesas_pagar),
            ("Despesas Comprometido", despesas_comprometido, saidas_comprometido, span_indice_despesas_comprometido),
        ]
    return _montar

