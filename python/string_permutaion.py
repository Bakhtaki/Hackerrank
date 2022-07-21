"""Permutation an string."""


from itertools import permutations

# -----------------------------------------------------------------------------
# You are given a string S.
# Your task is to print all possible permutations of size k of the string in
# lexicographic sorted order.

# Input:
# A single line containing the string S and the integer value k.

# Output:
# Print the permutations of the string S on separate lines.
# -----------------------------------------------------------------------------

# Read the string S and the integer value k.
S, k = input().split()

# Permute the string S and print the permutations in lexicographic sorted order.
permutations_list = list(permutations(S, int(k)))

# Sort the permutations list in lexicographic order.
permutations_list.sort()

# Print the permutations.
for permutation in permutations_list:
    print(''.join(permutation), end='\n')



