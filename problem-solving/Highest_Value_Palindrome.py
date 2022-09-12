#!/bin/python3

import os

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#


def highestValuePalindrome(s, n, k):
    # Write your code here
    if k >= n:
        return '9'*n
    s = list(s)
    must_change = []
    for i in range(n//2):
        if s[i] != s[-1-i]:
            must_change.append(i)
            s[i] = s[-1-i] = max(s[i], s[-1-i])

    if len(must_change) < k:
        more = k - len(must_change)
        last = 0
        while more > 0:
            for i in range(last, n//2):
                if s[i] != '9':
                    if i in must_change:
                        more += 1
                    if more >= 2:
                        s[i] = s[-1-i] = '9'
                        more -= 2
                        break
            if i == n//2-1:
                break
            last = i+1
        if more >= 1 and n % 2 != 0:
            s[n//2] = '9'
        return ''.join(s)
    elif len(must_change) == k:
        return ''.join(s)
    else:
        return '-1'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
