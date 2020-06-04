#!/usr/bin/python3
"""
Write a function that reads n lines of a text file (UTF8) and prints it to
stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    reads n lines of a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding='utf-8') as myFile:
        if nb_lines <= 0:
            print(myFile.read(), end='')
            return

        lines = 0
        for line in myFile:
            lines += 1
        myFile.seek(0)
        if nb_lines >= lines:
            print(myFile.read(), end='')
            return
        else:
            n = 0
            while n < nb_lines:
                print(myFile.readline(), end='')
                n += 1
