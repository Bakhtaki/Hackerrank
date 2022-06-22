"""Interduction to sets."""

# -----------------------------------------------------------------------------
# Task:
# Calculate Average with Formula:
# Average = Sum of Distinct Values / Number of Distinct Values

# Function Description:
# Complete the function

# Return:
# float - Average rounded to 3 decimal places

# Input Format:
# The first line contains an integer, n,the size of the array.
# The second line contains n space-separated integers describing the array[i].

# Constraints:
# 1 <= n <= 100
# Sample Input:
# 5
# 1 1 2 2 3

# Sample Output:
# 2.000
# -----------------------------------------------------------------------------


def average(array):
    """Calculate average of array."""
    # Initialize variables
    sum_of_elements = 0
    count_of_elements = 0

    # Convert array to set to remove duplicates
    array = set(array)

    # Loop through array
    for element in array:
        sum_of_elements += element
        count_of_elements += 1
    avearge_of_elements = sum_of_elements / count_of_elements
    return round(avearge_of_elements, 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
