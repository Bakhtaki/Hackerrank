#!/bin/python3

import os

# Complete the jumpingOnClouds function below.


def jumpingOnClouds(c, k):
    energy = 100
    lenght = len(c)
    position = 0

    while True:
        position = (position + k) % lenght
        energy -= 1
        if c[position] == 1:
            energy -= 2
        if position == 0:
            break
    return energy


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
