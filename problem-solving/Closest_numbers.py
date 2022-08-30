#!/bin/python3

import os

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    arr.sort()
    temp = arr[len(arr)-1]
    brr = []
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] < temp:
            temp = arr[i+1] - arr[i]
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == temp:
            brr.append(arr[i])
            brr.append(arr[i+1])
    return brr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

