#!/bin/python3

import os
#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def superReducedString(s):
    # Write your code here
    ls = list(s)

    while True:
        for i in range(len(ls)):
            if i + 1 < len(ls) and ls[i] == ls[i + 1]:
                ls.pop(i)
                ls.pop(i)
                break
        else:
            break
    return ''.join(ls) if ls else 'Empty String'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
