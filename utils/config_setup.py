import json
import os
import toml
from typing import List

from pydantic import BaseModel


def master_config():
    current_path = os.path.join(os.path.dirname(__file__), "../config/master_config.json")
    with open(current_path) as mc_config:
        data = json.load(mc_config)
        return data


def config():
    current_path = os.path.join(os.path.dirname(__file__), "../config/")
    with open("/Users/rmarck/PycharmProjects/railguns-at-dawn/config/config.toml") as config_file:
        data = toml.load(config_file)
    return data


class MasterConfig(BaseModel):
    browser: str

