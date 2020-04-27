import math
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from selenium.webdriver import Remote

class BasePage:
    def __init__(self, browser: Remote, url: str) -> None:
        """Base class for the web page

        :param selenium.webdriver.Remote browser: Selenium WebDriver instance
        :param str url: Link to the page
        """
        super().__init__()
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(10)

    def open(self) -> None:
        """Open the given web page in the browser

        :return: None
        """
        self.browser.get(self.url)

    def is_element_present(self, how: str, what: str) -> bool:
        """

        :param how:
        :param what:
        :return:
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False

        return True

    def solve_quiz_and_get_code(self) -> None:
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    #элемент не появляется на странице в течение заданного времени. Упадет, как только увидит искомый элемент. Не появился:тест зеленый.
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    #ожидаем, что элемент исчезает
    def is_disappeared(self, how, what, timeout=20):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        


