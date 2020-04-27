import pytest
from .pages.product_page import ProductPage
import time


# pytest -v -s --tb=line --language=en test_product_page.py

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)])
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip
def test_guest_can_add_product_to_cart(browser, link) -> None:
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    #time.sleep(10)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # Открываем страницу товара
    page.add_to_cart()                # Добавляем товар в корзину
    #time.sleep(60)
    #page.solve_quiz_and_get_code()      # Вводим в alert расчитанный код
    page.should_not_be_success_message()#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
@pytest.mark.skip
def test_user_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # Открываем страницу товара
    page.should_not_be_success_message()#Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    #return True
@pytest.mark.skip    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)   # Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                         # Открываем страницу товара
    page.add_to_cart()                # Добавляем товар в корзину
    #page.solve_quiz_and_get_code()      # Вводим в alert расчитанный код
    page.should_be_success_message_disappeared()               #Проверяем, что нет сообщения об успехе с помощью is_disappeared

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    #time.sleep(10)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()
    product_page.should_be_login_link()
    


