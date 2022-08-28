#!/bin/python3

import os

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#


def gemstones(arr):
    # Write your code here
    
    minerals = {}
    count = 0
    
    for element in arr:
        element = list(set(element))
        for each in element:
            if each in minerals.keys():
                minerals[each] += 1
            else:
                minerals[each] = 1
    for _,value in minerals.items():
        if value == len(arr):
            count += 1
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
