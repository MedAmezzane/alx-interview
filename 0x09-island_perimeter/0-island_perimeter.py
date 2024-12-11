#!/usr/bin/python3
"""
Defines a function to calculate the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A grid representing the map,
                 where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)       # Number of rows in the grid
    cols = len(grid[0])    # Number of columns in the grid
    perimeter = 0          # Initialize perimeter counter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Check if the current cell is land
                # Check top boundary or if the cell above is water
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # Check left boundary or if the cell to the left is water
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # Check bottom boundary or if the cell below is water
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # Check right boundary or if the cell to the right is water
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
