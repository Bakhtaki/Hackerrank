'''Solution for HackerRank problem "find_all and finditer"'''

# ----------------------------------------------------------------
# Task:
# You are given a string S . It consists of alphanumeric characters,
# spaces and symbols(+, -).
# Your task is to find all the substrings of S that:
# contains 2 or more vowels.
# Also, these substrings must lie in between 2
# consonants and should contain vowels only.
# Vowels are defined as: AEIOU and aeiou.
# Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

# Input Format:
# A single line of input containing string S.

# Constraints:
# 0 < len(S) < 100

# # Output Format:
# Print the matched substrings in their order of occurrence
# on separate lines.If no match is found, print -1.

# Sample Input:
# rabcdeefgyYhFjkIoomnpOeorteeeeet

# Sample Output:
# ee
# Ioo
# Oeo
# eeeee
# ----------------------------------------------------------------
import re

s = input()
pattern = (r'(?<=\w)([aeiouAEIOU]{2,})(?=\w)')

target = []
target.extend(re.findall(pattern, s))

if len(target) == 0:
    print(-1)
else:
    for _ in target:
        print(_, end='\n')
