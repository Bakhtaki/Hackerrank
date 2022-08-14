#!/bin/python3
import os

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#


def minimumNumber(n, password):
    """ Return the minimum number of characters to make the password strong"""
        special_characters = "!@#$%^&*()-+"
        count = 0
        if any(i.isdigit() for i in password) == False:
            count += 1
        if any(i.islower() for i in password) == False:
            count +=1
        if any(i.isupper() for i in password) == False:
            count +=1
        if any(i in special_characters for i in password) == False:
            count += 1
        return max(count, 6 - n)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
