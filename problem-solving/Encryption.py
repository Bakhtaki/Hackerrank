#!/bin/python3

import math
import os


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def encryption(s):
    # Write your code here
    s = s.replace(' ', '')
    len_s = len(s)
    encryption = []

    col = math.ceil(math.sqrt(len_s))

    for i in range(col):
        encryption.append(s[i::col])

    return ' '.join(encryption)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
