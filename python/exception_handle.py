"""Script for Exception Handling."""

# -----------------------------------------------------------------------------
# Task:
# You are given to values.
# # perform integer division and print the result.

# Input Format:
# The first line contains an integer, T
# T lines follow, each containing 2 space-separated integers.

# Output Format:
# For each test case, print the result of the integer division.
# If division by zero occurs, print error code

# Sample Input:
# 2
# 1 0
# 2 1
# Sample Output:
# error code - integer division or modulus by zero
# -----------------------------------------------------------------------------

# Read T:
t = int(input())
list_of_values = []

# Loop through T:
for i in range(t):
    a, b = input().split()

    # Save values to list:
    list_of_values.append([a, b])

for _i in list_of_values:
    try:
        a = int(_i[0])
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '{}'".format(_i[0]))
        continue
    try:
        b = int(_i[1])
    except ValueError:
        print("Error Code: invalid literal for int() with base 10: '{}'".format(_i[1]))
        continue

    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
