'''Solution for HackerRank problem "Validating Postal Code"'''
# -----------------------------------------------------------------------------
# Task:
# A valid postal code P must meet the following criteria:
# 1- P must be a number in the range from 100000 to 999999 inclusive.
# 2- P must not contain more than one alternating repetitive digit pair.
#
# Alternating repetitive digits are digits which repeat immediately after the
# next digit. In other words, an alternating repetitive digit pair is formed by
# two equal digits that have just a single digit between them.
#
# For example:
# 121426  # Here, 1 is an alternating repetitive digit.
# 523563  # Here, NO digit is an alternating repetitive digit.
# 552523  # Here, both 2 and 5 are alternating repetitive digits.
#
# Your task is to provide two regular expressions regex_integer_in_range and
# regex_alternating_repetitive_digit_pair.where:

# regex_integer_in_range should match only integers that are in the range
# 100000 to 999999 inclusive.

# regex_alternating_repetitive_digit_pair should find all alternating
# repetitive digits pairs in a string.

# both these regular expressions are to be used by the provide
# code template to check if the input string P is a valid postal code.
# Using the following expression:
#
# (bool(re.match(regex_integer_in_range, P))
# and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
#
# Input Format:
# Locked stub code in the editor reads a single string denoting P
# from stdin and uses provided expression and your regular expressions
# to validate if P is a valid postal code
#
# Output Format:
# You are not responsible for printing anything to stdout.
# Locked stub code in the editor does that.
#
# Sample Input:
# 110000
#
# Sample Output:
# False
# -----------------------------------------------------------------------------
# Solution:
import re

# Match only digits in the range 100000 to 999999 inclusive
regex_integer_in_range = r"^[1-9]\d{5}$"
# Regex to find alternating repetitive digits pairs
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
