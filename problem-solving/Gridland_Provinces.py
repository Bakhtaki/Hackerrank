"""Hackerrank Solution for Gridland Province."""
import os
#
# Complete the 'gridlandProvinces' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#


def gridlandProvinces(s1, s2):
    """Write your code here."""
    pass


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        s1 = input()

        s2 = input()

        result = gridlandProvinces(s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()
