"""
Solution for union of two sets.
Hacker Rank problem: https://www.hackerrank.com/challenges/py-set-union/problem
"""
#_______________________________________________________________________________
# Task:
# The students of District College have subscriptions to English and French
# newspapers. Some students have subscribed only to English,
# some have subscribed to only French and some have subscribed to both newspapers.
#
# You are given two sets of student roll numbers.
# One set has subscribed to the English newspaper, and the other set is subscribed
# to the French newspaper. The same student could be in both sets. Your task is to
# find the total number of students who have subscribed to at least one newspaper.
# Input Format
#
# The first line contains an integer,N, the number of students who have subscribed to the English newspaper.
# The second line contains N space separated roll numbers of those students.
# The third line contains B , the number of students who have subscribed to the French newspaper.
# The fourth line contains B space separated roll numbers of those students.
#
# Constraints
# 0 < Total number of students in college < 1000
#
# Output Format
# Output the total number of students who have at least one subscription.
#
# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8
#
# Sample Output
# 13
# -------------------------------------------------------------------------------
# Solution:
#
# 1. Create a set of students who have subscribed to English.
# 2. Create a set of students who have subscribed to French.
# 3. Find the union of the two sets.
# 4. Print the number of students in the union.
#
# _______________________________________________________________________________
#
# Read the number of students who have subscribed to English.
n = int(input())
# Read the students who have subscribed to English.
english_students = set(map(int, input().split()))

# Read the number of students who have subscribed to French.
b = int(input())
# Read the students who have subscribed to French.
french_students = set(map(int, input().split()))

# Find the union of the two sets.
union_students = english_students.union(french_students)

# Print the number of students in the union.
print(len(union_students))
# _______________________________________________________________________________
