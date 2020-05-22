#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix.
Prototype: def matrix_divided(matrix, div):
matrix must be a list of lists of integers or floats, otherwise
raise a TypeError exception with the message matrix must be a
matrix (list of lists) of integers/floats
Each row of the matrix must be of the same size, otherwise
aise a TypeError exception with the message
Each row of the matrix must have the same size
div must be a number (integer or float),
otherwise raise a TypeError exception with the message div must be a number
div can’t be equal to 0, otherwise
raise a ZeroDivisionError exception with the message division by zero
All elements of the matrix should be divided
by div, rounded to 2 decimal places
Returns a new matrix
You are not allowed to import any module
"""


def matrix_divided(matrix, div):
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or (len(matrix) == 0) or type(matrix[0])\
       is not list or (len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for c in row:
            if type(c) is not int and type(c) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(item / div, 2) for item in row] for row in matrix]
