"""
Find word accurance and count  in a sting.
retun -1 if not found.
"""
# 2 Integers: n and m.
# there are N words in group A which may be repeat.
# There are M words blong to group B.
# For each word in group B, find the number of occurrences in group A.
# Retutn -1 if not found.

# Import Modules
from collections import defaultdict

# Read input from STDIN.
n, m = map(int, input().split())

# Define Group A , Group B
words_a = []
words_b = []

# Read Words for group A from STDIN.
for i in range(n):
    words_a.append(input())

# Read Words for group B from STDIN.
for i in range(m):
    words_b.append(input())

# for each word in group B, print the position of the word in group A.
for word in words_b:
    positions = []
    for i in range(n):
        if word == words_a[i]:
            positions.append(i + 1)
    if len(positions) == 0:
        positions.append(-1)
    for position in positions:
        print(position, end=' ')
    print()
