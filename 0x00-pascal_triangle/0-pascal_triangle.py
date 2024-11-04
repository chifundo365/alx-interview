#!/usr/bin/python3
""" Implements the pascal's_triangle """


def pascal_triangle(n):
    """ Returns Pascal's Triangle """
    triangle = []

    for row in range(n):
        if row == 0:
            triangle.append([1])
        elif row == 1:
            triangle.append([1, 1])
        else:
            last_row = triangle[-1]
            new_row = []
            new_row.append(1)

            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i + 1])
            new_row.append(1)
            triangle.append(new_row)
    return triangle
