#!/bin/python3

import os

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def equalizeArray(arr):
    # Write your code here
    pairs = {}

    for i in arr:
        if i in pairs:
            pairs[i] += 1
        else:
            pairs[i] = 1

    max_value = max(pairs.values())

    return len(arr) - max_value


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
