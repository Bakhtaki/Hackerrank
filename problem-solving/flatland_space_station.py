#!/bin/python3

import os


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    """Write Your Code Here."""
    c = sorted(c)
    res = c[0]

    for ind in range(1, len(c)):
        res = max(res, (c[ind] - c[ind-1])//2)

    res = max(res, n-1 - c[-1])

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
