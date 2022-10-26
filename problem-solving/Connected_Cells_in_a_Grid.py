#!/bin/python3

import os

#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def connectedCell(matrix):
    # Write your code here
    def dfs(matrix, i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
            return 0
        matrix[i][j] = 0
        return 1 + dfs(matrix, i-1, j-1) + dfs(matrix, i-1, j) + dfs(matrix, i-1, j+1) + dfs(matrix, i, j-1) + dfs(matrix, i, j+1) + dfs(matrix, i+1, j-1) + dfs(matrix, i+1, j) + dfs(matrix, i+1, j+1)

    max_region = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                region = dfs(matrix, i, j)
                max_region = max(max_region, region)
    return max_region

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()

