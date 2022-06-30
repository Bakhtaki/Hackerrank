"""Script for set add solution"""
# -----------------------------------------------------------------------------
# Task:
# Rupal has a huge collection of country stamps.
# She decided to count the total number of distinct country stamps
# in her collection.
# She asked for your help. You pick the stamps one by one from a stack of
# N country stamps.
#
# Input Format:
# The first line contains an integer N , the total number of country stamps.
# The next N lines contains the name of the country where the stamp is from.

# Constraint
# 0 < N < 1000
#
# Output Format:
# Output the total number of distinct country stamps on a single line.
#
# Sample Input:
# 7
# UK
# GERMANY
# UK
# UK
# SPAIN
# FRANCE
# MEXICO
# Sample Output:
# 5
# -----------------------------------------------------------------------------
# Solution:
# -----------------------------------------------------------------------------
# Initialize a set and add the first country stamp.
# Loop through the remaining country stamps and add them to the set.
# Print the length of the set.
# -----------------------------------------------------------------------------
n = int(input())
contries = set()

for i in range(n):
    contries.add(input())

print(len(contries))
