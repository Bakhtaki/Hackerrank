#!/bin/python3

import os

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    u = n - r_q
    d = r_q-1
    r = n - c_q
    l = c_q-1
    ru = min(u, r)
    rd = min(r, d)
    lu = min(l, u)
    ld = min(l, d)

    for o in obstacles:
        if o[1] == c_q:
            if o[0] < r_q:
                d = min(d, r_q-1-o[0])
            else:
                u = min(u, o[0]-r_q-1)
        elif o[0] == r_q:
            if o[1] < c_q:
                l = min(l, c_q-1-o[1])
            else:
                r = min(r, o[1]-c_q-1)
        elif abs(o[0]-r_q) == abs(o[1]-c_q):
            if o[1] > c_q:
                if o[0] > r_q:
                    ru = min(ru, o[1]-c_q-1)
                else:
                    rd = min(rd, o[1]-c_q-1)
            else:
                if o[0] > r_q:
                    lu = min(lu, c_q-1-o[1])
                else:
                    ld = min(ld, c_q-1-o[1])

    return u + d + r + l + ru + rd + lu + ld


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
