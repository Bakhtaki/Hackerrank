'''Solution to the "Validate UID" challenge from hackerrank.com'''
# -----------------------------------------------------------------------------
# ABCXYZ company has up to 100  employees.
# The company decides to create a unique identification number(UID)
# for each of its employees.
# The company has assigned you the task of validating all the
# randomly generated UIDs.
#
# A valid UID must follow the rules below:
#
# It must contain at least 2 uppercase English alphabet characters.
# It must contain at least 3 digits(0-9).
# It should only contain alphanumeric characters(a-z,A-Z&0-9).
# No character should repeat.
# There must be exactly 10 characters in a valid UID.
#
# Input Format
#
# The first line contains an integer T, the number of test cases.
# The next T lines contains an employee's UID.
#
# Output Format
# For each test case, print 'Valid' if the UID is valid. Otherwise,
# print 'Invalid', on separate lines. Do not print the quotation marks.
#
# Sample Input
# 2
# B1CD102354
# B1CDEF2354
#
# Sample Output:
# Invalid
# Valid
# -----------------------------------------------------------------------------
import re


for _ in range(int(input())):
    u = ''.join(sorted(input()))

    uu = re.search(r'[A-Z]{2}', u)
    dd = re.search(r'\d\d\d', u)
    rr = re.search(r'[^a-zA-Z0-9]', u)
    hh = re.search(r'(.)\1', u)
    ll = len(u) == 10

    if (uu and dd and ll) and (not rr) and (not hh):
        print('Valid')
    else:
        print('Invalid')