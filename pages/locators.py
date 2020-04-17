from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
class ProductPageLocators:
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, "div.alertinner")
    ALERT_CART_STATUS = (By.CSS_SELECTOR, ".alert-noicon.alert-info p")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
