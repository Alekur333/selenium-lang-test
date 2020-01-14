import pytest
import time

def test_add_to_basket_button_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    add_to_basket_button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert add_to_basket_button > 0, "Кнопка 'Добавить в корзину' не найдена"


