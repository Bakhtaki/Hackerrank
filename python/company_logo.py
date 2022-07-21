"""Solution for the following problem:
   Hackerrank.com, Python Preparation Company Logo
"""
# ---------------------------------------------------------------
# Task
# Given a string , which is the company name in lowercase letters,
# your task is to find the top three most common characters in the string.
# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical
# order
# For Example Google would have the following output:
# G,O,E
#
# Input Format
# A single line of input containing the string S.
#
# Constraints
# 3 <= |S| <= 10^4
# S has at least 3 distinct characters.
# Output Format
# Print the three most common characters along with their occurrence count.
# if the occurrence count is the same, sort the characters in alphabetical
# order.
#
# Sample Input:
# aaabcccccaaa
#
# Sample Output
# a 6
# b 3
# c 6
# -----------------------------------------------------------------------
# Solution
# Import the collections module.
from collections import Counter

# Read the input.
s = input()
# Count each characters in string
for i in range(len(s)):
    c = Counter(s)

# Sort Dictionary keys alphabetical if values are equal.
sorted_c = sorted(c.items(), key=lambda x: (-x[1], x[0]))

# Print the top three most common characters.
for i in range(3):
    print(sorted_c[i][0], int(sorted_c[i][1]))
