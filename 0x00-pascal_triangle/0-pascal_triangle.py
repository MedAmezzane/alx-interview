#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to level n.

    Args:
        n (int): The number of levels in Pascal's triangle.

    Returns:
        list: A list of lists, where each sublist represents a level in
        Pascal's triangle.

    Example:
        pascal_triangle(4) ->
        [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1]
        ]
    """
    triangle = []  # Initialize list to store Pascal's triangle

    if n > 0:
        # Loop through each row from 1 to n
        for row in range(1, n + 1):
            current_row = []  # Initialize list for the current row
            coefficient = 1  # Start binomial coefficient at 1

            # Generate each element in the row
            for element in range(1, row + 1):
                current_row.append(coefficient)
                coefficient = coefficient * (row - element) // element

            triangle.append(current_row)  # Append the current row

    return triangle
