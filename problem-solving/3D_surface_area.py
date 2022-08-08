#!/bin/python3

import os

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#


def surfaceArea(a):
    # Write your code here
    s = 0
    for k in range(len(a)):
        for i in range(len(a[k])):
            back = min(a[k][i], a[k][i-1]) if i > 0 else 0
            side = min(a[k][i], a[k-1][i]) if k > 0 else 0
            s += 2 + a[k][i]*4 - back*2 - side*2
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
