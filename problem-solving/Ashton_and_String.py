#!/bin/python3

import os
#
# Complete the 'ashtonString' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def ashtonString(s, k):
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        k = int(input().strip())

        res = ashtonString(s, k)

        fptr.write(str(res) + '\n')

    fptr.close()
