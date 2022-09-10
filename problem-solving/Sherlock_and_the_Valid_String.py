#!/bin/python3

import os

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    # Write your code here
    counts = {}

    for each in s:
        if each in counts:
            counts[each] += 1
        else:
            counts[each] = 1
    return 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
