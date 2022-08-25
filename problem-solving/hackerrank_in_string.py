#!/bin/python3

import os

#
# Complete the 'hackerrankInString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def hackerrankInString(s):
    # Write your code here
    h = "hackerrank"
    n = -1
    for x in range(len(h)):
        try:
            n = s.index(h[x], n+1)
        except:
            return "NO"

    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
