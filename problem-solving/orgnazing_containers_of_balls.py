#!/bin/python3

import os

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#


def organizingContainers(container):
    # Write your code here
    caps = []
    for i in range(len(container)):
        caps.append(sum(container[i]))

    typenums = []
    for i in range(len(container)):
        n = 0
        for j in range(len(container)):
            n += container[j][i]
        typenums.append(n)

    if sorted(caps) == sorted(typenums):
        return 'Possible'
    else:
        return 'Impossible'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
