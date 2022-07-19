'''Solution for validating phone number HackerRank.com'''
# -----------------------------------------------------------------------
# Let's dive into the interesting topic of regular expressions!
# You are given some input, and you are required to check whether
# they are valid mobile numbers.
# A valid mobile number is a ten digit number starting with a 7,8 or 9.

# Input Format
# The first line contains an integer, the number of inputs.
# lines follow, each containing some string.

# Constraints
# 1 <= N <= 10
# 2 <= length of string <= 15

# Output Format
# For every string listed, print "YES" if it is a valid mobile number
# and "NO" if it is not on separate lines. Do not print the quotes.

# Sample Input
# 2
# 9587456281
# 1252478965

# Sample Output
# YES
# NO
# -----------------------------------------------------------------------
import re

n = int(input())
for i in range(n):
    # regex Pattern for 10 digit mobile numbers starting with 7,8 or 9
    mobile = input()
    pattern = re.compile(r'^[789]\d{9}$')

    if re.match(pattern, mobile):
        print("YES")
    else:
        print("NO")
