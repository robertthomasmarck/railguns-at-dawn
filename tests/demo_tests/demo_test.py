# Implementation of Selenium WebDriver with Python using PyTest
import pytest
from selenium.webdriver.common.by import By
from time import sleep
from pages.google_search_page import GoogleSearchPage
from pages.instagram_search_page import InstagramAccountPage
from pages.twitter_account_page import TwitterAccountPage
from pages.twitter_search_page import TwitterSearchPage

from tests.base_test import BaseTest


class TestDemo(BaseTest):

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

    def test_twitter(self):
        twitter_search_page = TwitterSearchPage(self.driver)
        twitter_account_page = TwitterAccountPage(self.driver)

        assert_list = []

        twitter_search_page.goto()
        twitter_search_page.search_twitter("Ryan Reynolds")
        twitter_search_page.click_person("@VancityReynolds")
        expected_account_title = 'Ryan Reynolds (@VancityReynolds) / Twitter'
        account_title = twitter_account_page.get_account_title()
        if not expected_account_title in account_title:
            assert_list.append(f"'{expected_account_title}' is not in {account_title}.")

        assert not assert_list, assert_list

    def test_instagram(self):
        instagram_search_page = InstagramAccountPage(self.driver)
        assert_list = []
        instagram_search_page.goto_account("jj.trailwalker")


