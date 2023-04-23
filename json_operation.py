import json
import os
from json import JSONDecodeError


def read_json(file_name: str):
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as f:
                json_data = json.load(f)
                return json_data
        except JSONDecodeError:
            return {}


def write_json(json_data: dict, file_name: str):
    with open(file_name, "w") as file_json:
        json.dump(json_data, file_json)
