import pytest

import os

from tests.webdriver_setup import build_browser
from utils import config_setup
from utils.config_setup import MasterConfig

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope='session')
def init_driver(main_config):

    if main_config.browser == "chrome":
        web_driver = build_browser("chrome")
    elif main_config.browser == "firefox":
        web_driver = build_browser("firefox")

    yield web_driver

    web_driver.quit()

@pytest.fixture(scope="session")
def main_config(request):
    _json = config_setup.master_config()
    config = MasterConfig(**_json)

    cli_browser = request.config.getoption('--browser')
    if cli_browser:
        config.browser = cli_browser

    cli_browser_options = request.config.getoption('--options')
    if cli_browser_options:
        config.options = [option.strip() for option in cli_browser_options.split(',')]

    cli_version = request.config.getoption('--driver_version')
    if cli_version:
        config.version = cli_version

    cli_driver_exe_path = request.config.getoption('--driver_exe_path')
    if cli_driver_exe_path:
        config.driver_exe_path = cli_driver_exe_path

    global cli_ring_central
    cli_ring_central = request.config.getoption('--ringC')

    return config

