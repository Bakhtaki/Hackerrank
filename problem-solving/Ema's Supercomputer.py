#!/bin/python3

import os
from itertools import combinations


#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#


def twoPluses(grid):
    # Write your code here
    h, w = len(grid), len(grid[0])
    plus = []
    def isGood(r, c): return grid[r][c] == 'G'
    def how(x): return 2*x-1
    mm = min(h, w)
    for step in range(1, mm // 2 + (1 if mm % 2 else 0)):
        for r in range(step, h-step):
            for c in range(step, w-step):
                if isGood(r, c):
                    s1 = {(r2, c)
                          for r2 in range(r-1, r-step-1, -1) if isGood(r2, c)}
                    s2 = {(r2, c)
                          for r2 in range(r+1, r+step+1, +1) if isGood(r2, c)}
                    s3 = {(r, c2)
                          for c2 in range(c-1, c-step-1, -1) if isGood(r, c2)}
                    s4 = {(r, c2)
                          for c2 in range(c+1, c+step+1, +1) if isGood(r, c2)}
                    if len(s1) == step and len(s2) == step and\
                            len(s3) == step and len(s4) == step:
                        plus.append(
                            (how(2*step+1), {(r, c)} | s1 | s2 | s3 | s4))
    if not plus:
        return 1
    if len(plus) == 1:
        return plus.pop()[0]
    combs = [s1*s2 for (s1, a), (s2, b)
             in combinations(plus, 2) if a.isdisjoint(b)]
    return max(combs) if combs else plus.pop()[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
