#!/usr/bin/python3
"""
Write a function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(obj, att, val):
    """
    Add new attrib if is possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, val)
