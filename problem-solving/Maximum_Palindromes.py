#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#


def initialize(s):
    # This function is called once before all queries.
    pass

    #
    # Complete the 'answerQuery' function below.
    #
    # The function is expected to return an INTEGER.
    # The function accepts following parameters:
    #  1. INTEGER l
    #  2. INTEGER r
    #

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
