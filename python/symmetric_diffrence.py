"""Symmetric Difference of two sets"""

# ---------------------------------------------------------------------
# Task
# You are 2 given sets of integers.M and N.
# Print the symmetric difference of the two sets.
# The symmetric difference of two sets is the set of elements
# which are in one of the sets, but not in both.
#
# Input Format
# The first line an integer M,denoting the number of elements in the first set
# The second line contains M space separated integers.
# The third line an integer N.
# The fourth line contains N space separated integers.
#
# Output Format
# Output the symmetric difference in ascending order.

# Sample Input
# 4
# 2 4 5 9
# 3
# 2 4 11 12
#
# Sample Output
# 1
# 3
# 5
# 6
# --------------------------------------------------------------------
# Solution

# Read input
m = int(input())
set_a = set(map(int, input().split()))

n = int(input())
set_b = set(map(int, input().split()))


# Calculate symmetric difference
symmetric_difference = set_a.symmetric_difference(set_b)

# Print output in ascending order
for i in sorted(symmetric_difference):
    print(i)
