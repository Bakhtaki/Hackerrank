#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    """ Write your code here."""
    x = set(s)
    m = 0
    l = list(map(set,combinations(x,2)))

    for i in l:
        y = x - i
        z = s
        for j in y:
            z = z.replace(j, "")
        r = ("".join(i)) * (len(z) // 2)
        if r + r[0] == z or z == r or r == z[::-1] or r[1] + r == z:
            m = max(m, len(z))
    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
