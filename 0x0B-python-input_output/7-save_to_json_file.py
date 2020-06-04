#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Write a function that writes an Object to a text file, using a JSON
representation:
"""
import Json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, "w", encoding='utf-8') as myFile:
        myFile.write(json.dumps(my_obj))
