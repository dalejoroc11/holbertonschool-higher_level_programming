#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Write a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    fun reads a text file (UTF8) and prints it to
    stdout
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
