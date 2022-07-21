"""Solution for no ideal problem."""

# ---------------------------------------------------------------------
# Array of N integers
# 2 disjoint sets of integers M integers
# Initial Happiness = 0
# Goal = Find final happiness
# if integer is in set A then happiness += 1
# if integer is in set B then happiness -= 1
# if integer is not in set A or B then happiness won't change
# since A and B are set of integers, we there is no duplicate integers
#
# Constraints:
# 1 <= N <= 10^5
# 1 <= M <= 10^5
# 1 <= A[i] <= 10^9
#
# Input Format:
# The first line contains an integer N, the number of integers.
# The second line contains N space-separated integers A[i].
# The third nad fourth line contains an integer M, the number of sets.
#
# Sample Input:
# 5
# 1 2 3 4 5
# 2
# 1 2
# Output Format:
# Print the final happiness.
# ---------------------------------------------------------------------
# Import Section

# Variables Section
integers = []

# Read Count of Integers N , M
n, m = map(int, input().split())

# Read N Elements of Array
integers = list(map(int, input().split()))

# Read M Elements of Sets A and B
set_a = list(map(int, input().split()))
set_b = list(map(int, input().split()))

# Convert to Set
A = set(set_a)
B = set(set_b)

# initialize happiness
happiness = 0

for element in integers:
    if element in A:
        happiness += 1
    if element in B:
        happiness -= 1
# Print Happiness
print(happiness)
