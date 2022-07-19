'''Solution to the regex start end problem Hackerrank.com'''
# -----------------------------------------------------------------------------
# Task:
# You are given a string s
# Your task is to find indices of the start and end of string k in the string s
# Input Format:
# The first line contains the string s.
# The second line contains the string k.
#
# Constraints:
# 0 < len(s) < 100
# 0 < len(k) < len(s)
#
# Output Format:
# Print the tuple in this format: (start, end)
# if no match is found, print (-1, -1)
#
# Sample Input:
# aaadaa
# aa
# Sample Output:
# (0, 1)
# (1, 2)
# (4, 5)
# -----------------------------------------------------------------------------
import re

# Read input
S = input()
K = input()

m = re.search(K, S)
pattern = re.compile(K)

if not m:
    print((-1, -1))
while m:
    print("({}, {})".format(m.start(), m.end()-1))
    m = pattern.search(S, m.start()+1)
