#!/bin/python3

import os

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Write your code here
    len_s = len(s)
    middle = len_s // 2

    if len_s % 2 == 1:
        return -1
    first = s[:middle]
    second = s[middle:]

    for letter in first:
        if letter in second:
            second = second.replace(letter, '', 1)
    return len(second)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()

