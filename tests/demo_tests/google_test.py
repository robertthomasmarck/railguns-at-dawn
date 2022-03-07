# Implementation of Selenium WebDriver with Python using PyTest
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pages.google_search_page import GoogleSearchPage

from tests.base_test import BaseTest


class TestGoogle(BaseTest):

    def test_lambdatest_google(self):
        search_page = GoogleSearchPage(self.driver)
        title = search_page.get_title()
        if not "Google" in title:
            raise Exception("Could not load page")
        search_page.fill_out_text_field("Robert Marck")
        search_page.click_google_search()
        # Check if the LambdaTest Home Page is open
        search_page.click_web_element((By.XPATH, "//h3[contains(text(), 'Robert Marck - Software Developer')]"))
        sleep(5)
        last_title = search_page.get_title()
        assert last_title == ""


