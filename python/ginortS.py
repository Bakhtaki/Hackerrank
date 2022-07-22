""""Solution For ginortS Hackerrank.com/challenges/ginorts/problem."""

# --------------------------------------------------------------------------------------
# You are given a String Solution.
# S Contains alphanumeric characters only.
# Your task is to sort the string in the following manner:
# All sorted lowercase letters are ahead of uppercase letters.
# all sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
#
# Input Format:
# A single line of input contains the string S.
#
# Constraints
# 0 < len(S) < 1000
#
# Output Format:
# Output the sorted string S.
#
# Sample Input:
# Sorting1234
#
# Sample Output:
#
# ginortS1234
# --------------------------------------------------------------------------------------
# Read String
S = input()

lw = []
for c in S:
    if c.isalpha() and c.islower():
        lw.append(c)
lw.sort()

up = []
for c in S:
    if c.isupper():
        up.append(c)
up.sort()

od = []
for n in S:
    if n.isdigit() and int(n) % 2 == 1:
        od.append(n)
od.sort()

ev = []
for n in S:
    if n.isdigit() and int(n) % 2 == 0:
        ev.append(n)
ev.sort()


print(''.join(lw + up + od + ev))
