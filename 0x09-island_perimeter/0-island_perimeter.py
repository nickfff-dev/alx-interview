#!/usr/bin/python3
"""This module defines a function to calculate the perimeter of an island in a
2D grid."""


def island_perimeter(grid):
    """Calculates the perimeter of an island represented by '1's surrounded by
    water ('0's).

    Parameters:
    grid (list of list of int): The grid representing the map.

    Returns:
    int: The perimeter of the island.
    """
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                # Check the cell to the north
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check the cell to the south
                if i == height - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check the cell to the west
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check the cell to the east
                if j == width - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
