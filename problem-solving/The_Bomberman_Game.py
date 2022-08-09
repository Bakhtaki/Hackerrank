#!/bin/python3
import os

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


def bomberMan(n, grid):
    # Write your code here
    if n == 1:
        return grid

    if n % 2 == 0:
        return [r.replace(".", "O") for r in grid]

    thirdGrid = explodeBomb(grid)
    fithGrid = explodeBomb(thirdGrid)
    return fithGrid if ((n - 1) / 2) % 2 == 0 else thirdGrid


def explodeBomb(grid):
    R = len(grid)
    C = len(grid[0])

    neighbours = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
    transformedGrid = [list(r) for r in grid]
    fullGird = [["O"] * C for _ in range(R)]

    bombs = locateBomb(transformedGrid)
    # printGrid(grid, b="Initial")

    for b in bombs:
        for n in neighbours:
            if 0 <= b[0] + n[0] < R and 0 <= b[1] + n[1] < C:
                fullGird[b[0] + n[0]][b[1] + n[1]] = "."

    return ["".join(r) for r in fullGird]


def locateBomb(grid):
    locations = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                locations.append((i, j))
    return locations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
