#!/usr/bin/python3
"""Doc"""
import json


def load_from_json_file(filename):
    """Doc"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
