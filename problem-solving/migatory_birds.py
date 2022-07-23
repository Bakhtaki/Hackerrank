#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here
    pairs = {}

    for i in arr:
        if i in pairs:
            pairs[i] += 1
        else:
            pairs[i] = 1

    max_pair = max(pairs.values())
    max_pair_keys = [k for k, v in pairs.items() if v == max_pair]

    return min(max_pair_keys)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
