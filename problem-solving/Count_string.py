#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING r
#  2. INTEGER l
#


def countStrings(r, l):
    # Write your code here
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        r = first_multiple_input[0]

        l = int(first_multiple_input[1])

        result = countStrings(r, l)

        fptr.write(str(result) + '\n')

    fptr.close()
