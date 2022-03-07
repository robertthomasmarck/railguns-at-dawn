from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class GoogleSearchPage(BasePage):
    Q = By.NAME, "q"
    title = "Most Powerful Cross Browser Testing Tool Online | LambdaTest"

    def __init__(self, driver):
        super().__init__(driver)
        self.url = self.config['base_urls']['google']

    def goto(self):
        self.goto_page(self.url)

    def click_google_search(self):
        self.click_web_element(self.Q)

    def click_search_result(self, by_locator):
        self.click_web_element(by_locator)



