#!/usr/bin/python3
"""
Write a function that prints a text with 2 new
lines after each of these characters: ., ? and :
Prototype: def text_indentation(text):
text must be a string, otherwise raise a TypeError
exception with the message text must be a string
There should be no space at the beginning or at the end of each printed line
You are not allowed to import any module
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print()
