#!/bin/python3

import os

# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#


def absolutePermutation(n, k):
    # Write your code here
    if k == 0:
        return [i+1 for i in range(n)]
    elif n % (2*k) != 0 or 2*k > n:
        return [-1]
    return [(i+1)+(1 if (i//k) % 2 == 0 else -1)*k for i in range(n)]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
