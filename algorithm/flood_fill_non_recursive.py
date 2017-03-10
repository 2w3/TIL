#!/usr/bin/env python
# coding=utf-8
import numpy as np

matrix = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
]

def flood_fill_non_recursive(matrix, x, y):
    stack = []
    stack.append((x, y))

    while len(stack) > 0 :
        x, y = stack.pop()
        if matrix[x][y] != 0:
            continue
        matrix[x][y] = 1

        if (x+1) < len(matrix):
            stack.append( ( x+1, y ) )

        if (x-1) >= 0:
            stack.append( ( x-1, y ) )

        if (y+1) < len(matrix[x]):
            stack.append( ( x, y + 1 ) )

        if (y-1) >= 0:
            stack.append( ( x, y - 1 ) )

print("before matrix")
print(np.array(matrix))
flood_fill_non_recursive(matrix, 1, 2)
print("after matrix")
print(np.array(matrix))
