import time

from typing import List
from typing import Optional
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from config.TestData import TestData
import os


class Browser:
    """Browser ENUMS"""
    CHROME = 'chrome'
    FIREFOX = 'firefox'
    EDGE = 'edge'


def build_browser(browser, experimental_options: Optional[List[dict]], browser_options: List[str]):
    if browser == Browser.CHROME:
        options = build_browser_options(Browser.CHROME, browser_options, experimental_options)
        return webdriver.Chrome(ChromeDriverManager(version="latest").install(),
                                executable_path=TestData.CHROME_EXECUTABLE,
                                service_log_path=os.path.devnull,
                                options=options)


def build_browser_options(browser, browser_options: List[str], experimental_options: Optional[List[dict]]):
    browser = browser.lower()
    if browser == Browser.CHROME:
        options = webdriver.ChromeOptions()
        if experimental_options:
            for exp_option in experimental_options:
                options.add_experimental_option("prefs", exp_option)

    else:
        raise ValueError(f'{browser} is not supported')

    for option in browser_options:
        options.add_argument(f'--{option}')

    return options
