"""Solution For Hackerrank.com/challenges/any-or-all/problem"""
# --------------------------------------------------------------------------------------
# Task
#
# You are given a space separated list of integers.
# If all the integers are positive,
# then you need to check if any integer is a palindromic integer.
#
# Input Format
# The First line contains an integer N.
# N is the total number of integers in the list.
# The Second line contains N space separated integers.
#
# Constraints
# 0 <= N <= 100
#
# Output Format
# Print True if all the conditions of the problem statement are satisfied.
#
# Sample Input
# 5
# 12 9 61 5 14
#
# Sample Output
# True
# --------------------------------------------------------------------------------------
N = int(input())
arr = list(map(int, input().split()))
print(all(x > 0 for x in arr) and any([str(i) == str(i)[::-1] for i in arr]))
