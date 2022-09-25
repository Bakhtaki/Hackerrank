"""Hackerrank Solution ProblemSolving/Build a String."""
import os

#
# Complete the 'buildString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. STRING s
#


def buildString(a, b, s):
    """Write your code here."""
    i = 1
    l = len(s)
    cost = 0
    cost = [float('inf')] * (l + 1)
    cost[0] = 0
    k = 0
    while i <= l:
        j = max(i, k)
        while j <= l and (s[i-1:j] in s[:i-1]):
            j += 1
        if j-1 != i:
            cost[j-1] = min(cost[i-1] + b, cost[j-1])
            k = j
        cost[i] = min(cost[i-1] + a, cost[i])
        i += 1

    return (cost[-1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        a = int(first_multiple_input[1])

        b = int(first_multiple_input[2])

        s = input()

        result = buildString(a, b, s)

        fptr.write(str(result) + '\n')

    fptr.close()
