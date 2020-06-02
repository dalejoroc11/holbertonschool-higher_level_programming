#!/usr/bin/python
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """
    Class MyList inherits from list
    """
    def print_sorted(self):
        """
        list sorted
        """
        print(sorted(self))
