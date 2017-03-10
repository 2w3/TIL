#!/usr/bin/env python
# coding=utf-8


matrix = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

def flood_fill(matrix, x, y):
    if matrix[x][y] != 1:
        matrix[x][y] = 1

        if (x+1) < len(matrix):
            flood_fill(matrix, x+1, y)

        if (x-1) >= 0:
            flood_fill(matrix, x-1, y)

        if (y+1) < len(matrix[x]):
            flood_fill(matrix, x, y+1)

        if (y-1) >= 0:
            flood_fill(matrix, x, y-1)


print("before matrix")
print(matrix)
flood_fill(matrix, 1, 2)
print("after matrix")
print(matrix)
