"""Script for Deque data structure."""
# -----------------------------------------------------------------------------
# TASk:
# Perform append, pop, popleft and appendleft methods on an empty deque .
#
# Input Format:
# The first line contains an integer,N
# The next N lines contains separated names of the methods and their values.
#
# Constraints:
# 0 < N < 100
#
# Output Format:
# print space separated values of the methods.
#
# Sample Input:
# 5
# append 1
# append 2
# appendleft 3
# pop
# popleft
#
# Sample Output:
# 1 2
# -----------------------------------------------------------------------------
# Solution:
# Import the deque class from the collections module.
from collections import deque

d = deque()

# Read the number of operations from the first line.
n = int(input())

for i in range(n):
    inp = input().split()
    if len(inp) == 1:
        if inp[0] == 'pop':
            d.pop()
        elif inp[0] == 'popleft':
            d.popleft()
    else:
        if inp[0] == 'append':
            d.append(inp[1])
        elif inp[0] == 'appendleft':
            d.appendleft(inp[1])
# Print the deque.
print(' '.join(d))
