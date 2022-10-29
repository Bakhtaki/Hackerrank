#!/bin/python3
import os

# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#


# Define Function to check next point is accessible or not
def check_accessibility(matrix, point, visited):
    (x, y) = point
    n = len(matrix)
    m = len(matrix[0])
    next_point = []

    for (i, j) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= x + i < n and \
            0 <= y + j < m and matrix[x + i][y + j] != 'X'\
                and (x + i, y + j) not in visited:
            next_point.append((x + i, y + j))
    return next_point


def countLuck(matrix, k):
    # Write your code here
    # Find Start and end point
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'M':
                start = (row, col)
            if matrix[row][col] == '*':
                end = (row, col)
    visited = {}
    current = [(start, 0)]

    while current:
        next_points = []
        for (x, y), step in current:
            if (x, y) == end:
                return 'Impressed' if step == k else 'Oops!'
            if (x, y) not in visited:
                visited[(x, y)] = True
                next_point = check_accessibility(matrix, (x, y), visited)
            count = 1 if len(next_point) >= 2 else 0
            for (i, j) in next_point:
                next_points.append(((i, j), step + count))
        current = next_points


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
