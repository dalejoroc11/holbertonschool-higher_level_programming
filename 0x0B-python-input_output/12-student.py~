#!/usr/bin/python3
"""
Write a class Student that defines a student by: (based on 11-student.py)
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
        __init__ student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        get dictionary with info Student
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
