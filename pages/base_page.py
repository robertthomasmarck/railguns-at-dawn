from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from utils import config_setup


class BasePage:

    def __init__(self, driver, config=config_setup.config()):
        self.driver = driver
        self.config = config

    def goto_page(self, page_url):
        self.driver.get(page_url)

    def get_title(self):
        return self.driver.title

    def get_web_element(self, by_locator, wait=10):
        try:
            el = WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(by_locator))
        except TimeoutException:
            print("Wait for element timed out")
            el = self.driver.find_element(*by_locator)
        return el

    def fill_out_text_field(self, by_locator, value):
        el = self.get_web_element(by_locator)
        el.click()
        el.clear()
        el.send_keys(value)

    def click_web_element(self, by_locator):
        self.get_web_element(by_locator).click()

    def press_return(self):
        ActionChains(self.driver).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()