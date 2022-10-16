#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoTwo' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING a as parameter.
#

def twoTwo(a):
    # Write your code here
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        result = twoTwo(a)

        fptr.write(str(result) + '\n')

    fptr.close()

