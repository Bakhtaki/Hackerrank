#!/bin/python3

import os
from collections import deque
#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def knightlOnAChessboard(n):
    """Write your code here."""
    # Define Function to check all possible moves
    def check_pairs(a, b, x, y, n):
        valid_moves = {}
        # Check all possible valid_moves
        possible_moves = [(a + x, b + y), (a - x, b - y),
                            (a + x, b - y), (a - x, b + y),
                            (a + y, b + x), (a - y, b - x),
                            (a + y, b - x), (a - y, b + x)]

        for move in possible_moves:
            if  0 <= move[0] < n  and 0 <= move[1] < n:
                valid_moves[move] = 1

        return valid_moves

    # Define breadth first search function
    def bfs(x, y, n):
        queue = deque([(0, 0, 0)])
        visited = {}

        while queue:
            a, b, count = queue.popleft()
            possible_pairs = check_pairs(a, b, x , y, n)
            for pair in possible_pairs:
                if pair == (n-1, n-1):
                    return count + 1
                if pair not in visited:
                    visited[pair] = 1
                    queue.append((pair[0], pair[1], count + 1))
        return -1

    result = []
    for i in range(1, n):
        temp = []
        for j in range(1, n):
            temp.append(bfs(i, j, n))
        result.append(temp)
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

