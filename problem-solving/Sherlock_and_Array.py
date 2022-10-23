#!/bin/python3

import os
#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    if len(arr) == 1:
        return "YES"

    left = 0
    right = sum(arr[1:])

    for i in range(1, len(arr)):
        if left == right:
            return "YES"
        left += arr[i-1]
        right -= arr[i]

        if left > right:
            break

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

