#!/bin/python3

import math
import os
import random
import re
import sys
from tkinter.messagebox import NO
from turtle import st

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#


def matrixRotation(matrix, r):
    # Write your code here
        m, n = len(matrix), len(matrix[0])
    b = [[None] * n for _ in range(m)]
    indices = []

    for c in range(min(m,n) // 2):
        index = []

        for i in range(c,n - c ):index.append((c,i))
        for i in range(c + 1,m - c - 1):index.append((i,n - c - 1))
        for i in range(c, n - c)[::-1]:index.append((m - c - 1,i))
        for i in range(1 + c, m -1- c)[::-1]:index.append((i,c))

        if not index:
            break
        indices.append(index)

    rotated  = []
    for index in indices:
        k = r % len(index)
        rotated.append(index[k:] + index[:k])

    for (x, y) in zip(indices, rotated):
        for (c ,d),(e, f) in zip(x, y):
            b[c][d] = matrix[e][f]

    for each in b:
        print(''.join(str(x) for x in each), end='\n')



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
