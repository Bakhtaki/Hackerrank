'''Solution to the regex substitution problem Hackerrank.com'''
# -----------------------------------------------------------------------------
# Task:
# You are given a text of N lines. The text contains && and || symbols.
# Yor task is to modify those symbols to the following:
# -&& -> and
# || -> or
# Both && and || should have a space on both sides.
#
# Input Format:
# The First line contains an integer N.
# The next N lines contains the text.

# Constraints:
# 0 < N < 100

# Output Format:
# Output the modified text.
#
# Sample Input:
# 11
# a = 1
# b = input()
# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))

# Note do not change &&& or ||| or & or |
# Only change those '&&' which have space on both sides.
# Only change those '|| which have space on both side

# Sample Output:
# a = 1
# b = input()

# if a + b > 0 and a - b < 0:
#     start()
# elif a*b > 10 or a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))

# #Note do not change &&& or ||| or & or |
# #Only change those '&&' which have space on both sides.
# #Only change those '|| which have space on both sides
# -----------------------------------------------------------------------------
import re

N = int(input())

# Read the Next N lines of the input
for i in range(N):
    line = input()
    while ' && ' in line or ' || ' in line:
        line = re.sub(r' && ', ' and ', line)
        line = re.sub(r' \|\| ', ' or ', line)
    print(line)
