from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TwitterSearchPage(BasePage):

    SEARCH_BAR = (By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")

    def __init__(self, driver, title="Twitter"):
        super().__init__(driver)
        self.url = self.config['base_urls']['twitter']
        self.title = title

    def goto(self):
        self.goto_page(self.url)

    def search_twitter(self, search):
        self.fill_out_text_field(self.SEARCH_BAR, search)
        self.press_return()

    def click_person(self, person):
        self.click_web_element((By.XPATH, f"//span[contains(text(), '{person}')]"))
