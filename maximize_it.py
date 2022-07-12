"""Solution for HackerRank/maximize_it."""
# -----------------------------------------------------------------------------
# You are given function f(x) = x^2. You are also given K Lists.
# The ith  list consists of Ni elements.
# You have to pick one element from each list so that the vale of equation
# below is maximized:
# S = (f(x1) + f(x2) + ... + f(xk)) % M
# xi denotes the ith element of the list.
# % denotes the modulo operator.
# Note that you need to take exactly one element from each list,
# not necessarily the largest element. You add the squares of the chosen elements
# and perform the modulo operation. The maximum value that you can obtain, will be
# the answer to the problem
#
# Input Format
# The first line contains 2 space separated integers K and M.
# the next K lines each contain an integer Ni,
# denoting the number of elements in the list.
# Followed by Ni space separated integers denoting the elements in the list.
#
# Constraints
# 1 <= K <= 7
# 1 <= M <= 1000
# 1 <= Ni <= 7
# 1 <= Magnitude of elements in list <= 10 ^ 9
#
# Output Format
# Single integer denoting the value of Smax.
#
# Sample Input
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
#
# Sample Output
# 206
# -----------------------------------------------------------------------------
from itertools import product

# Read M,K
all_list = []

K,M = map(int, input().split())

# Read K List of elements
for i in range(K):
    all_list.append(list(map(int, input().split()[1:])))

for i in range(len(all_list)):
    for j in range(len(all_list[i])):
        all_list[i][j] = all_list[i][j] ** 2


Max = 0
for t in product(*all_list):
   sum_t = sum(t) % M
   if sum_t > Max:
       Max = sum_t

print(Max)