#!/bin/python3
import os
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def runningTime(arr):

    """Write your code here."""
    n = len(arr)
    result = 0

    for i in range(1, n):
        target = arr[i]
        j = i - 1
        while (j >= 0) and (arr[j] > target):
            arr[j + 1] = arr[j]
            result += 1
            j -= 1
        arr[j + 1] = target

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
