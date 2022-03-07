from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GoogleSearchPage(BasePage):
    Q = (By.NAME, "q")

    def __init__(self, driver, title="Google"):
        super().__init__(driver)
        self.url = self.config['base_urls']['google']
        self.title = title

    def goto(self):
        self.goto_page(self.url)

    def fill_out_search(self, value):
        self.fill_out_text_field(self.Q, value)

    def press_enter_for_search(self):
        self.press_return()

    def search_for(self, value):
        self.fill_out_search(value)
        self.press_enter_for_search()

    def click_search_result(self, result):
        self.click_web_element((By.XPATH, f"//h3[contains(text(), '{result}')]"))






