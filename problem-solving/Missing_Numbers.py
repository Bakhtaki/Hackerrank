#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    dict_brr = {}

    for element in brr:
        if element in dict_brr:
            dict_brr[element] += 1
        else:
            dict_brr[element] = 1

    for element in arr:
        if element in dict_brr:
            dict_brr[element] -= 1

    result = []
    for key, value in dict_brr.items():
        if value > 0:
            result.append(key)

    return sorted(result)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

