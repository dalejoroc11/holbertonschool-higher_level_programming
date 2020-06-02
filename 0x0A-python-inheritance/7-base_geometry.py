#!/usr/bin/python3
"""
Write a class BaseGeometry (based on 6-base_geometry.py).
"""


class BaseGeometry():
    """
    T6: Class BG exception
    """
    def area(self):
        """
        Not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        T7: public instance validate value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
