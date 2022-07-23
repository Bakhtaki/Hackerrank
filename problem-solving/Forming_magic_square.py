#!/bin/python3

import os

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def formingMagicSquare(s):
    # Write your code here
    orig = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    all_squares = [orig]
    all_squares.append(orig[::-1])
    all_squares.append([i[::-1] for i in orig])
    all_squares.append(all_squares[2][::-1])
    all_squares.append([[4, 3, 8], [9, 5, 1], [2, 7, 6]])
    all_squares.append(all_squares[4][::-1])
    all_squares.append([i[::-1] for i in all_squares[4]])
    all_squares.append(all_squares[6][::-1])

    least = 99
    for i in all_squares:
        temp = 0
        for j in range(3):
            for k in range(3):
                temp += abs(s[j][k]-i[j][k])
        if temp < least:
            least = temp

    return least


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
