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


def build_browser(browser, browser_options: List[str]):
    if browser == Browser.CHROME:
        options = build_browser_options(Browser.CHROME, browser_options)
        return webdriver.Chrome(ChromeDriverManager(version="latest").install(),
                                service_log_path=os.path.devnull,
                                options=options)


def build_browser_options(browser, browser_options: List[str]):
    browser = browser.lower()
    if browser == Browser.CHROME:
        options = webdriver.ChromeOptions()

    else:
        raise ValueError(f'{browser} is not supported')

    for option in browser_options:
        options.add_argument(f'--{option}')

    return options
