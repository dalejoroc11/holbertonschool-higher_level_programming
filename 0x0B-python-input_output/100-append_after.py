#!/usr/bin/python3
"""
Write a function that inserts a line of text to a file, after each line
containing a specific string (see example):
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing a specific
    string
    """
    text = ""
    with open(filename, "r", encoding='utf-8') as myFile:
        for line in myFile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding='utf-8') as newFile:
        newFile.write(text)
