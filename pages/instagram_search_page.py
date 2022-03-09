from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InstagramAccountPage(BasePage):

    SEARCH_BAR = (By.XPATH, "")

    def __init__(self, driver, title="Twitter"):
        super().__init__(driver)
        self.url = self.config['base_urls']['instagram']
        self.title = title

    def goto_account(self, account):
        self.goto_page(self.url + "/" + account + "/")

    def search_twitter(self, search):
        self.fill_out_text_field(self.SEARCH_BAR, search)
        self.press_return()

    def click_person(self, person):
        self.click_web_element((By.XPATH, f""))
