#!/usr/bin/python3
"""
Write a function that multiplies 2 matrices:
Read: Matrix multiplication - only Matrix product (two matrices)
Prototype: def matrix_mul(m_a, m_b):
m_a and m_b must be validated with these requirements in this order
m_a and m_b must be an list of lists of integers or floats:
"""


def max_integer(list=[]):
    """
    Function to find and return the max integer in a list of integers
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
