'''Solution to the challenge "reduce function" from the "Python Challenge'''
# -----------------------------------------------------------------------------
# Given a list of rational numbers,find their product.
#
# Input Format:
# first line contains n , the number of rational numbers in the list.
# the oth of next line contains two integers each,the numerator(Ni) and
# denominator(Di) of ith the rational number in the list.
#
# Output Format:
# Print only one line containing the numerator and denominator of the product
# of all the rational numbers in the list in the simplest form.
# i.e numerator and denominator have no common divisor other than 1.
#
# Constraints:
# 1<=n<=100
# 1<=Ni,Di<=10^9
#
# Sample Input:
# 3
# 1 2
# 3 4
# 10 6
#
# Sample Output:
# 5 8
# -----------------------------------------------------------------------------
from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)




