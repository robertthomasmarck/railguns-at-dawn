import pytest

from utils import config_setup


@pytest.mark.usefixtures("init_driver")
class BaseTest:

    @staticmethod
    def master_config():
        file = config_setup.master_config()
        return file
