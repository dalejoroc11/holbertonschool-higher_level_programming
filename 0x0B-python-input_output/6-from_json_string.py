#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Write a function that returns an object (Python data structure) represented
by a JSON string
"""
import Json


def from_json_string(my_str):
    """
    returns an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
