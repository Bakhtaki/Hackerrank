"""Find incorrect regexes in the input string."""


# -----------------------------------------------------------------------------
# TASK:
# You are given a string S.
# Your task is to find out whether S is a correct regex or not.

# Input Format:
# The first line contains an integer T, the number of test cases.
# The next T lines contains the string S.

# Output Format:
# Print true if S is a correct regex, else print false.

# Constraints:
# 1 <= T <= 100

# Sample Input:
# 2
# .*\+
# .*+
# Sample Output:
# true
# false

# Explanation:
# .\*+ is a correct regex.
# .\*+ is not a correct regex.
# -----------------------------------------------------------------------------

# Imports
import re

# list for storing the input strings
input_strings = []

# reat first line of input
t = int(input())

# Read strings from input
for i in range(t):
    input_strings.append(input())

# Check if the strings is correct regex statement or not
for element in input_strings:
    try:
        re.compile(element)
        print(True)
    except re.error:
        print(False)








