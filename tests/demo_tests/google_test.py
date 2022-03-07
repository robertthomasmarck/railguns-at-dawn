# Implementation of Selenium WebDriver with Python using PyTest
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from pages.google_search_page import GoogleSearchPage

from tests.base_test import BaseTest


class TestGoogle(BaseTest):

    @pytest.mark.synthetic
    def test_google(self):
        search_page = GoogleSearchPage(self.driver)
        assert_list = []

        search_page.goto()
        title = search_page.get_title()
        expected_title_1 = "Google"
        if not expected_title_1 in title:
            assert_list.append(f"Title is not {title}.")
        search_page.search_for("Robert Marck")
        # Check if the LambdaTest Home Page is open
        search_page.click_search_result("Robert Marck - Software Developer")
        last_title = search_page.get_title()
        expected_title_2 = "Robert Marck - Software Developer In Test - PlanSource"
        if not expected_title_2 in last_title:
            assert_list.append(f"{expected_title_2} is not in {last_title}.")
        assert not assert_list, assert_list
