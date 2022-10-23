#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

def minimumLoss(price):
    # Write your code here
    # Create a dictionary to store the price and index
    price_index = {}
    for i in range(len(price)):
        price_index[price[i]] = i

    # Sort the price_index
    price_index = sorted(price_index.items(), key=lambda x: x[0])

    # Find the minimum minimumLoss
    min_loss = sys.maxsize

    for i in range(len(price_index) - 1):
        if price_index[i][1] > price_index[i + 1][1]:
            min_loss = min(min_loss, price_index[i + 1][0] - price_index[i][0])

    return min_loss


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()

