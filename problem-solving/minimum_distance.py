#!/bin/python3

import os
import sys


# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    min_dist = sys.maxsize

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                min_dist = min(min_dist, j-i)
    if min_dist == sys.maxsize:
        return -1
    else:
        return min_dist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
