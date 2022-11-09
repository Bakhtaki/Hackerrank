#!/bin/python3
"""Hackerrank Making Candies."""

import math
import os


#
# Complete the 'minimumPasses' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER m
#  2. LONG_INTEGER w
#  3. LONG_INTEGER p
#  4. LONG_INTEGER n
#


def minimumPasses(m, w, p, n):
    """Hackerrank Making Candies."""
    # Write your code here
    # m =  number of machines
    # w = number of workers
    # p = cost of a new resource
    # n = number of candies to be produced( target)

    days = 1
    candies = m * w
    max_days = math.ceil(n/(m * w))
    resource = 0

    while candies < n:
        if candies < p:
            req_days = math.ceil((p-candies)/(m*w))
            candies += req_days * m * w
            days += req_days
            continue
        # buy resource
        resource, candies = divmod(candies, p)
        total = m+w+resource
        half = total//2
        if m > w:
            m = max(m, half)
            w = total - m
        else:
            w = max(w, half)
            m = total - w
        candies = candies+m*w
        days += 1
        max_days = min(max_days, days + math.ceil((n - candies) / (m * w)))
        # print(candies,days)

    return min(max_days, days)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    w = int(first_multiple_input[1])

    p = int(first_multiple_input[2])

    n = int(first_multiple_input[3])

    result = minimumPasses(m, w, p, n)

    fptr.write(str(result) + '\n')

    fptr.close()
