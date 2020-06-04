#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Write a function that returns the JSON representation of an object (string)
"""
import Json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)
    """
    return json.dumps(my_obj)
