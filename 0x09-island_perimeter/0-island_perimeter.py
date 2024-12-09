#!/usr/bin/python3
""" Insland perimeter solution """


def island_perimeter(grid):
    """ Finds the perimeter meter of the island in the grid """
    perimeter = 0
    for i in range(len(grid)):
        for x in range(len(grid[i])):
            if grid[i][x] == 1:
                left = x - 1
                right = x + 1
                top = i - 1
                bottom = i + 1

                if left < 0 or grid[i][left] == 0:
                    perimeter = perimeter + 1
                if right == len(grid[i]) or grid[i][right] == 0:
                    perimeter += 1
                if top < 0 or grid[i][top] == 0:
                    perimeter += 1
                if bottom == len(grid[i]) or grid[i][bottom] == 0:
                    perimeter += 1
    return perimeter
