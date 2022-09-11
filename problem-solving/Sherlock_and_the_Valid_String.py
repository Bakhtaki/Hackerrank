#!/bin/python3

import os
from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    # Write your code here
    res = list(Counter(list(Counter(s).values())).values())
    if len(res) == 1:
        return "YES"
    if len(res) > 2:
        return "NO"
    if len(res) == 2:
        c = res.pop()
        if c > 1:
            return "NO"
        else:
            return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
