'''Solution for validating the credit card number HackerRank.com'''
# -----------------------------------------------------------------
# Task:
# Verify whether his credit card numbers are valid or not.
# A Valid credit card number has the following format:
#
# it must start with a 4, 5 or 6.
# it must contain exactly 16 digits.
# it must contain only digits (0-9).
# it must have digits in groups of 4, separated by one hyphen "-".
# it must Not use any other separator like ' ' , '_', etc.
# it must Not have 4 or more consecutive repeated digits.
#
# Example:
# valid credit card numbers:
# 4253625879615786
# 4424424424442444
# 5122-2368-7954-3214
#
# Invalid credit card numbers:
# 42536258796157867       #17 digits in card number → Invalid
# 4424444424442444        # digits are repeating 4 or more times → Invalid
# 5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
# 44244x4424442444        #Contains non digit characters → Invalid
# 0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
#
# Input Format:
# The first line of input contains an integer n.
# The next N lines contain credit card numbers.
#
# Constraints:
# 0 < N < 100
#
# Output Format:
# Print "Valid" if the credit card number is valid.Otherwise, print "Invalid".
#
# Sample Input
# 6
# 4123456789123456
# 5123-4567-8912-3456
# 61234-567-8912-3456
# 4123356789123456
# 5133-3367-8912-3456
# 5123 - 3567 - 8912 - 3456
#
# Sample Output
# Valid
# Valid
# Invalid
# Valid
# Invalid
# Invalid
# -----------------------------------------------------------------------
# Solution
import re

TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")

for _ in range(int(input().strip())):
    print("Valid" if TESTER.search(input().strip()) else "Invalid")
