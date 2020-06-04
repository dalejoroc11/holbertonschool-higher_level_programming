#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Create a function def pascal_triangle(n): that
returns a list of lists of integers representing
the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Creates a pascal triangle
    """
    pascal = []
    triangle = []

    for i in range(int(n)):
        new = pascal[:]
        new.append(1)
        pos = len(pascal)
        for i in range(1, pos):
            new[i] = pascal[i - 1] + pascal[i]
        pascal = new[:]
        triangle.append(pascal)
    return triangle
