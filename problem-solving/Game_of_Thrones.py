#!/bin/python3

import os

#
# Complete the 'gameOfThrones' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def gameOfThrones(s):
    # Write your code here
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    odd = 0
    for i in d:
        if d[i] % 2 != 0:
            odd += 1
    if odd > 1:
        return "NO"
    else:
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
