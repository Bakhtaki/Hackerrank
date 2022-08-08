#!/bin/python3

import os

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#


def strangeCounter(t):
    # Write your code here
    n = 3

    while t > n:
        t -= n
        n *= 2

    return n - t + 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
