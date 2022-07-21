"""Test Script for Combination of Substring with itertools."""


# Importing the libraries
from itertools import combinations

# -----------------------------------------------------------------------------
# Description:
# You are given a string S.
# Your task is to print all possible substrings of size k in lexicographic
# order.

# input format:
# The first line contains the string S and integer k separated by a space.
# The sting contains only uppercase letters A-Z.
# The string S is not empty.

# output format:
# Print all possible substrings of size k in separated lines.
# -----------------------------------------------------------------------------

# Reading the input
s, k = input().split()

# upper case the string
s = s.upper()

# SORT the string
s = sorted(s)

# Combination of Substring for all values less than k
for i in range(1, int(k) + 1):
    for j in combinations(s, i):
        print(''.join(j))
