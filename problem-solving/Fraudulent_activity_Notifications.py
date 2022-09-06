#!/bin/python3

import os
from bisect import bisect_left, insort
#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def my_med(arr,m,d):
    if d % 2 == 0:
        return sum(arr[m-1:m+1]) /2
    else:
        return arr[m]


def activityNotifications(expenditure, d):
    # Write your code here
    count = 0
    ex_len = len(expenditure)
    tr = sorted(expenditure[0:d])
    m = d // 2

    for i in range(d,ex_len):
        if expenditure[i] >= 2 * my_med(tr, m, d):
            count += 1
        del tr[bisect_left(tr,expenditure[i-d])]
        insort(tr,expenditure[i])
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
