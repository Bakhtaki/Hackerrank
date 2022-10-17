#!/bin/python3
import os
#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quickSort(arr):
    """Write your code here."""
    equal = []
    right = []
    left = []

    equal.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            left.append(arr[i])
        elif arr[i] > arr[0]:
            right.append(arr[i])
        else:
            equal.append(arr[i])
    sorted = left + equal + right
    return sorted


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
