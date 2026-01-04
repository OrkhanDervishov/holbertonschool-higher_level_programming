#!/usr/bin/python3
import json


def load_and_deserialize(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def serialize_and_save_to_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)
