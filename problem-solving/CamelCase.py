#!/bin/python3

import os

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def camelcase(s):
    # Write your code here
    words = 1

    for i in s:
        if i.isupper():
            words += 1
    return words


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
