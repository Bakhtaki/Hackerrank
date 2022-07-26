#!/bin/python3


#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#


def extraLongFactorials(n):
    # Write your code here
    # use bigint to avoid overflow
    if n == 0:
        return 0
    answer = 1

    while n > 0:
        answer *= n
        n -= 1
    return answer


if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
