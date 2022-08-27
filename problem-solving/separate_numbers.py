#!/bin/python3
#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    """Write your code here."""
    found = 0
    length = len(s)

    for x in range(1, (length // 2) + 1):
        index = x
        value = [s[:x]]

        while index < length:
            next_value = str(int(value[-1]) + 1)
            index += len(next_value)
            value.append(next_value)
        if ''.join(value) == s:
            found = value[0]
    print('YES {}'.format(found) if found else 'NO')


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
