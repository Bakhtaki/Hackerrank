#!/bin/python3
import os
from collections import Counter
import os
#
# Complete the 'buildPalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


def buildPalindrome(a, b):
    # Write your code here
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        a = input()

        b = input()

        result = buildPalindrome(a, b)

        fptr.write(result + '\n')

    fptr.close()
