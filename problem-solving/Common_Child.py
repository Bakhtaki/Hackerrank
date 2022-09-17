
# !/bin/python3

import os

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def commonChild(s1, s2):
    """Write your code here."""
    m = len(s1)
    n = len(s2)
    # 2D Array m*n
    counter = [[0] * (n + 1) for x in range(m + 1)]
    longest = 0

    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                c = counter[i][j] + 1
                counter[i + 1][j + 1] = c
                if c > longest:
                    longest = c
            else:
                counter[i + 1][j + 1] = max(counter[i + 1][j],
                                            counter[i][j + 1])
    return longest


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
