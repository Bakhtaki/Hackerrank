#!/bin/python3

import os
from bisect import bisect_right, insort
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#

def maximumSum(a, m):
    # Write your code here
    max_sum = 0
    sum_so_far = 0
    cum_sum = []

    for i in range(len(a)):
        sum_so_far = (sum_so_far + a[i]) % m
        position = bisect_right(cum_sum, sum_so_far)
        d = 0 if position == i else cum_sum[position]
        max_sum = max(max_sum, (sum_so_far - d + m) % m)
        insort(cum_sum, sum_so_far)

    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()

