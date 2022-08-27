import os
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#


def weightedUniformStrings(s, queries):
    """Write your code here."""
    all_Weight = set()
    count = 1

    for i in range(len(s)):
        if i+1 != len(s) and s[i] == s[i+1]:
            count += 1
        else:
            count = 1
        weight = (ord(s[i]) - 96)
        all_Weight.add(weight * count)
    return ["Yes" if w in all_Weight else "No" for w in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()

