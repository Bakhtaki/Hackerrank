#!/bin/python3

from math import gcd
from functools import reduce
import os


#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    lcm_a = reduce(lambda x, y: x * y // gcd(x, y), a)
    gcd_b = reduce(lambda x, y: gcd(x, y), b)
    return sum([1 for i in range(lcm_a, gcd_b + 1, lcm_a)
                if all(j % i == 0 for j in b)])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
