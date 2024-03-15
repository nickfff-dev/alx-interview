#!/usr/bin/python3
""" This module defines a pascal triangle function
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to row n.

    Parameters:
    n (int): The number of rows to generate in Pascal's Triangle.

    Returns:
    list of lists: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
