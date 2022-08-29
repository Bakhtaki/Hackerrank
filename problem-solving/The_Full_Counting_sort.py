#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    count_arr = {i:'' for i in range(100)}
    j = 0 
    for i in arr:
        if j < n // 2 :
            count_arr[int(i[0])] = count_arr[int(i[0])] +'-'
            j += 1
        else:
            count_arr [int(i[0])] = count_arr[int(i[0])] + i[1] + ''
    [print(x,end='') for x in count_arr.values() if x != '']


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
