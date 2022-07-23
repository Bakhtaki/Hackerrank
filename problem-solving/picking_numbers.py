#!/bin/python3
import os
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    # Write your code here
    a.sort()
    max_count = 0

    for i in range(len(a)):
        count = 1
        for j in range(i + 1, len(a)):
            if a[i] == a[j] or abs(a[i] - a[j]) == 1:
                count += 1
            else:
                break
        if count > max_count:
            max_count = count
    return max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
