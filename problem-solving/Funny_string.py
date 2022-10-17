#!/bin/python3
import os

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def funnyString(s):
    # Write your code here
    sums = []
    sums_rev = []
    for x in range(len(s)-1):
        diff = abs(ord(s[x]) - ord(s[x+1]))
        sums.append(diff)
    for y in range(len(s)-1, 0, -1):
        diff = abs(ord(s[y]) - ord(s[y-1]))
        sums_rev.append(diff)
    if sums == sums_rev:
        return('Funny')
    else:
        return "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
