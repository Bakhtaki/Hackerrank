#!/bin/python3
#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    kapers = []

    def checkKaper(i):
        count_of_digits = len(str(i))
        i_square = str(i * i)

        right_section = int(i_square[len(i_square) - count_of_digits:])
        left_section = i_square[:len(i_square) - count_of_digits]

        if left_section == '':
            left_section = 0
        else:
            left_section = int(left_section)
        return right_section + left_section == i

    for i in range(p, q+1):
        if checkKaper(i):
            kapers.append(i)

    if len(kapers) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(str(each) for each in kapers))


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
