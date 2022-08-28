#!/bin/python3

import os
#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    x = [0] * 100
    sorted_list = []
    
    for element in arr:
        x[element] += 1

    for i in range(len(x)):
        if x[i] > 0:
            for _ in range(x[i]):
                sorted_list.append(i)
    return sorted_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

