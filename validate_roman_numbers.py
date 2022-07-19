'''Solution for validating roman number HackerRank.com'''
# -----------------------------------------------------------------------------
# Task:
# You are given a string and you have to validate if it's a valid roman number.
# if it's valid, return true, otherwise return false.

# Input Format:
# A single string, containing a roman characters.

# Output Format:
# output string containing the True or False according to the question.

# Constraints:
# The number will be between 1 and 3999.(both included)

# Sample Input:
# CDXXI

# Sample Output:
# True
# -------------------------------------------------------------------------------
import re

regex_pattern = r"^ M{0, 3}(CM | CD | D?C{0, 3})?(XC | XL | \
    L?X{0, 3})?(IX | IV | V?I{0, 3})?$'"
print(str(bool(re.match(regex_pattern, input()))))
