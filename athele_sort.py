"""Sort Solution for HackerRank.com/challenges/athlete-sort/problem"""

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    # Print array after sorting
    x = sorted(arr, key=lambda x: x[k])
    for i in x:
        print(*i)
