#!/bin/python3

import os

#
# Complete the 'theLoveLetterMystery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def theLoveLetterMystery(s):
    # Write your code here
    L = len(s)
    l, r = L // 2, L // 2
    if L % 2 == 0:
        l, r = L//2-1, L//2-1
        r = L//2
    count = 0 
    while l >= 0 and r <= L - 1:
        count += abs(ord(s[l]) - ord(s[r]))
        l -= 1
        r += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()

