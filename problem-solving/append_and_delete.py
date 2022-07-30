#!/bin/python3

import os

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#


def appendAndDelete(s, t, k):
    # Write your code here"
    same = 0
    i = 0

    while i < len(s) and i < len(t) and s[i] == t[i]:
        same += 1
        i += 1

    s1 = len(s[i:])
    t1 = len(t[i:])

    if s1 + t1 > k:
        return "No"
    elif s1 + t1 == k:
        return "Yes"
    elif (len(s) + len(t)) - k <= 0:
        return "Yes"
    elif abs(len(s) + len(t) - k) % 2 == 0:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
