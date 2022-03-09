from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TwitterAccountPage(BasePage):

    def __init__(self, driver, title="Twitter"):
        super().__init__(driver)
        self.title = title

    def get_account_title(self):
        return self.get_title()




