#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#


def larrysArray(arr):
    # Write your code here
    a = [x - 1 for x in arr]
    swaps = 0
    i = 0
    while i < len(a)-1:
        if a[i] == i:
            i += 1
            continue
        tmp = a[i]
        a[i] = a[tmp]
        a[tmp] = tmp

        swaps += 1
    if swaps % 2 == 0:
        return("YES")
    else:
        return("NO")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        fptr.write(result + '\n')

    fptr.close()
