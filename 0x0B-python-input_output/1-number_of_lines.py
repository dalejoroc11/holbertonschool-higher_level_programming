#!/usr/bin/python3
"""
Write a function that returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """
    return number of lines of a text file
    """
    lines = 0
    with open(filename, "r", encoding='utf-8') as myFile:
        for line in myFile:
            lines += 1
    return lines
