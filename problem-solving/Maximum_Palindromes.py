#!/bin/python3

import os

maximum = 26


def initialize(s):
    global arr, fac, mod, M
    M = 1000000007
    n = len(s)
    arr = [[0 for _ in range(n + 1)] for _ in range(maximum)]
    for i in range(n):
        for j in range(maximum):
            arr[j][i + 1] = arr[j][i] + ((ord(s[i]) - 97) == j)
    fac = [1] * (n + 1)
    mod = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = (fac[i - 1] * i) % M
        mod[i] = pow(fac[i], M - 2, M)


def answerQuery(l, r):
    global arr, fac, mod, M
    odd = 0
    even = 0
    divs = 1
    for i in range(maximum):
        value = arr[i][r] - arr[i][l - 1]
        odd += (value & 1)
        even += (value // 2)
        divs = (divs * mod[value//2]) % M
    result = (fac[even] * divs) % M
    if (odd > 0):
        result = (result * odd) % M
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
