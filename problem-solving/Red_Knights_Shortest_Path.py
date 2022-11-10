#!/bin/python3
#
# Complete the 'printShortestPath' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER i_start
#  3. INTEGER j_start
#  4. INTEGER i_end
#  5. INTEGER j_end
#

def printShortestPath(n, i_start, j_start, i_end, j_end):
    # Print the distance along with the sequence of moves.

    # Start point
    start = (i_start, j_start)
    # End point
    end = (i_end, j_end)

    # Create a queue for BFS
    queue = [(start, [])]

    # Mark the squares visited
    visited = set()

    # Loop until the queue is empty
    while queue:
        next_move = []
        for (x, y), path in queue:
            if (x, y) == end:
                print(len(path))
                print(' '.join(path))
                return
            for i, j, direction in [(-2, -1, 'UL'), (-2, 1, 'UR'),
                                    (-1, -2, 'L'), (-1, 2, 'R'),
                                    (1, -2, 'L'), (1, 2, 'R'),
                                    (2, -1, 'UL'), (2, 1, 'UR')]:
                if 0 <= x+i < n and 0 <= y+j < n and (x+i, y+j) not in visited:
                    next_move.append(((x+i, y+j), path + [direction]))
                    visited.add((x+i, y+j))


if __name__ == '__main__':
    n = int(input().strip())

    first_multiple_input = input().rstrip().split()

    i_start = int(first_multiple_input[0])

    j_start = int(first_multiple_input[1])

    i_end = int(first_multiple_input[2])

    j_end = int(first_multiple_input[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
