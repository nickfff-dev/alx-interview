#!/usr/bin/python3
"""
Rotate a given 2D matrix 90 degrees clockwise in-place.

Parameters:
matrix (list[list[int]]): The 2D matrix to be rotated.

Returns:
None
"""


def rotate_2d_matrix(matrix):
    # Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row
    for row in matrix:
        row.reverse()
