#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromicBorder' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromicBorder(s):
    # Write your code here
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = palindromicBorder(s)

    fptr.write(str(result) + '\n')

    fptr.close()

