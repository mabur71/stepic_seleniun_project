'''1-й вариант
def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    go_to_login_page(browser) '''
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

'''def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    #page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина
    page.should_be_login_link()
'''
