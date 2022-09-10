#!/bin/python3

import os
#
# Complete the 'makingAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def makingAnagrams(s1, s2):
    # Write your code here
    s2 = list(s2)
    count = 0
    for letter in s1:
        if letter in s2:
            s2.remove(letter)
        else:
            count += 1
    return len(s2) + count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
