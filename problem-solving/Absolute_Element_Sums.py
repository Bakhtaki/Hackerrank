#!/bin/python3

import os
from collections import Counter

#
# Complete the 'playingWithNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries

def playingWithNumbers(arr, queries):
    # Write your code here
    # Seprate positive and negative numbers in the array
    positive_numbers = [element for element in arr if element >= 0]
    negative_numbers = [element for element in arr if element < 0]

    # Size of each array
    positive_size = len(positive_numbers)
    negative_size = len(negative_numbers)

    # Sort the arrays
    positive = sorted(Counter(positive_numbers).items(), reverse=True)
    negative = sorted(Counter(negative_numbers).items())

    # Initialize the Totol
    total = sum(abs(element) for element in arr)

    # Cumulative sum of queries
    cumulative_sum = 0

    # Loop through the queries
    for query in queries:
        # Add the query to the cumulative_sum
        cumulative_sum += query

        total += positive_size * query - negative_size * query

        # Loop through the positive queries
        if query > 0:
            while negative_size > 0 and negative[-1][0] < cumulative_sum:
                (n, count) = negative.pop()
                positive.append((n, count))
                positive_size += count
                negative_size -= count
                total += abs(n + cumulative_sum) * count * 2
        else:
            while positive_size > 0 and positive[-1][0] > cumulative_sum:
                (p, count) = positive.pop()
                negative.append((p, count))
                positive_size -= count
                negative_size += count
                total += abs(p + cumulative_sum) * count * 2
        yield total



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    q = int(input().strip())

    queries = list(map(int, input().rstrip().split()))

    result = playingWithNumbers(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

