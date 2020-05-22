#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats,
therwise raise a TypeError exception with the message matrix must be a matrix
(list of lists) of integers/floats
Each row of the matrix must be of the same size,
otherwise raise a TypeError exception with the
 message Each row of the matrix must have the same size
div must be a number (integer or float),
herwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise
raise a ZeroDivisionError exception with themessage division by zero
All elements of the matrix should be
divided by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module
"""


def say_my_name(first_name, last_name=""):
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is', first_name, last_name)
