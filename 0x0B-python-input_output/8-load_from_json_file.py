#!/usr/bin/python3
"""
Write a function that creates an Object from a “JSON file”:
"""
import Json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”:
    """
    with open(filename, "r", encoding='utf-8') as myFile:
        return json.load(myFile)
