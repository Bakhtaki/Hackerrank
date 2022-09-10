#!/bin/python3

import os
#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def argsort(arr):
    return sorted(range(len(arr)), key=lambda x: arr[x])


def lilysHomework(arr):
    len1 = len(arr)
    res = len1
    for _ in range(2):
        swaps = 0
        # Turn integers to consecutive integers
        arr = argsort(argsort(arr))
        visited = [False] * len1
        for i in range(len1):
            if visited[i]:
                continue
            visited[i] = True
            if i != arr[i]:
                j = arr[i]
                visited[j] = True
                while j != i:
                    j = arr[j]
                    swaps += 1
                    visited[j] = True
        res = min(res, swaps)
        if not _:
            arr.reverse()
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

