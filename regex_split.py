'''Solution For HackerRank Python Regex Split Challenge'''
#  ------------------------------------------------------------------------------
# You are given a string S consisting only of digits 0-9.,comma and dot.
# Your task is to complete the function regex_pattern defined below.
# which will be used to re.split() all of the , and . in the string S.
# It is guaranteed that every comma and dot in the string S is preceded
# and followed by a digit.
#
# Sample Input:
# 100,000,000.000
#
# Example Output:
# 100
# 000
# 000
# 000
# -----------------------------------------------------------------------------
import re
regex_pattern = r"[,.]+"  # Do not delete 'r'.

print("\n".join(re.split(regex_pattern, input())))
