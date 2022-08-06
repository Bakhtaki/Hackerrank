#!/bin/python3

import os

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#


def timeInWords(h, m):
    # Write your code here
    minutes = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
               'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen',
               'nineteen', 'twenty', 'twenty one', 'twenty two',
               'twenty three', 'twenty four', 'twenty five', 'twenty six',
               'twenty seven', 'twenty eight', 'twenty nine', 'thirty']

    hours = ['zero', 'one', 'two', 'three', 'four', 'five', 'six',
             'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']

    minute = int(m)
    hour = int(h)

    if minute == 0:
        return hours[hour] + ' o\' clock'
    if minute == 15:
        return 'quarter past ' + hours[hour]
    if minute == 30:
        return 'half past ' + hours[hour]
    if minute == 45:
        return 'quarter to ' + hours[hour + 1]
    if minute == 1:
        return minutes[minute] + ' minute past ' + hours[hour]
    if minute < 30:
        return minutes[minute] + ' minutes past ' + hours[hour]
    if minute > 30:
        return minutes[60 - minute] + ' minutes to ' + hours[hour + 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
