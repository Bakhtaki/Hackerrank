"""Try Combination with Replace"""

# -----------------------------------------------------------------------------
# Your Task:
# You are given a string as S.
# Your task is to print all possible combinations of size k in S.

# Input Format:
# A single line containing the string S and integer value k.

# Constraints:
# 0 < k < len(S)

# Output Format:
# Print the combinations of size k in S.

# Sample Input:
# HACK 2

# Sample Output:
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
# -----------------------------------------------------------------------------

# Import the necessary modules
from itertools import combinations_with_replacement


# Read the input
S, k = input().split()
S = sorted(S)

print(*[''.join(i) for i in combinations_with_replacement(S,
                                                          int(k))], sep='\n')
