#!/usr/bin/python3
"""
Module to rotate a 2D matrix in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list): The 2D matrix to rotate.
    """
    n = len(matrix)  # Get the size of the matrix.

    # Transpose the matrix.
    for row in range(n):
        for col in range(row, n):
            matrix[row][col], matrix[col][row] = (
                matrix[col][row],
                matrix[row][col]
            )

    # Reverse each row of the transposed matrix.
    for row in matrix:
        row.reverse()
