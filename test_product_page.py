from .pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser) -> None:
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart(True)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


def test_guest_can_add_non_promo_product_to_cart(browser) -> None:
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()
