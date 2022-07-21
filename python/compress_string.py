"""Compress a string using counts of repeated characters.
   We will use with itertools.groupby() to group characters together.
"""
# ---------------------------------------------------------------
# Task
# You are given a string S.Suppose a character 'C' occurs consecutively
# times in the string. Replace these consecutive occurrences of the character
# 'C' with  in the string.
#
# Input Format
# A single line containing the string S.
#
# Output Format
# Print the modified string.
#
# Constraints
# 1 <= |S| <= 10^4
#
# Sample Input
# aaabcccccaaa
#
# Sample Output
# (a,3),(b,1),(c,5),(a,3)
# ---------------------------------------------------------------
# Solution
from itertools import groupby

# Initialize the variables
result = []

# Read input
S = input()

for key, group in groupby(S):
    result.append((key, len(list(group))))

for each in result:
    print(each[0], int(each[1])), end = ' ')
