"""
A program to manage session data by loading from and saving to a JSON file,
with interactive user input for specific session values.

This script provides functionality to read session data from a file,
update session data based on user input, and save it back. Default values
are used when user input is empty. It includes utility functions to process
input and manage JSON data storage.
"""

import json


SESSION_FILE = "session.json"


def load_session_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    # except json.JSONDecodeError:
    #     return {}


def save_session_data(file_name, session_data):
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(session_data, f, indent=4)


def _get_val(s: str, val) -> int:
    return int(s) if len(s) > 0 else val


session_data = load_session_data(SESSION_FILE)
val1 = session_data.get("val1", 0)
val2 = session_data.get("val2", 0)

session_data["val1"] = _get_val(input(f"Число 1 (по умолчанию {val1}):) "), val1)
session_data["val2"] = _get_val(input(f"Число 2 (по умолчанию {val2}):) "), val2)
save_session_data(SESSION_FILE, session_data)
