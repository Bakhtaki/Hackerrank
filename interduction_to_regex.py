'''Solution For HackerRank Problem: Introduction to Regex.'''

# --------------------------------------------------------------
# You are given a string .
# Your task is to verify that is a floating point number.
# a valid float number must satisfy all of the following requirements:
#  Number can start with +, - or . symbol.
# For example:
# +4.50 True
# -1.0 True
# .5 True
# -.7 True
# +.4 True
# -+4.5 False
# Number must contain at least  decimal value.
# For example:
# 12. False
# 12.0 True
# Number must have exactly one . symbol.
# Number must not give any exceptions when converted using float(N).
#
# Input Format
# The first line contains T , the number of test cases.
# The next T is the a string, S.
#
# Constraints
# 1 < T < 10
#
# Output Format
# Output the answer for each test case in separate lines.
# --------------------------------------------------------------
# Import Modules
import re

T = int(input())
for test in range(T):
    S = input()
    if re.match(r'^[+-]?\d*\.\d+$', S):
        print('True')
    else:
        print('False')
