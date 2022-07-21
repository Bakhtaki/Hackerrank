'''Solution for the max script challenge HackerRank'''
# -----------------------------------------------------------------------------
# Neo has a complex matrix script.The matrix script is a N X M grid of strings.
# It consists of alphanumeric characters, spaces and symbols (!,@,#,$,%,&).
#
# To decode the script, Neo needs to read each column and select only the
# alphanumeric characters and connect them. Neo reads the column from top to
# bottom and starts reading from the leftmost column.
# If there are symbols or spaces between two alphanumeric characters of the
# decoded script, then Neo replaces them with a single space '' for better
# readability.
# Neo feels that there is no need to use 'if' conditions for decoding.
# Alphanumeric characters consist of: [A-Z, a-z, and 0-9].
#
# Input Format:
# The first line contains space separated integers N(rows) and M(columns)
# Respectively.
# The next N lines contain the row elements of the matrix script.
#
# Constraints:
# 0 < N,M < 100
# Note: 0 score will be awarded for using 'if' conditions in your code.
#
# Output Format:
# Print the decoded matrix script.
#
# Sample Input:
# 7 3
# Tsi
# h % x
# i
# sM
# $a
# #t%
# ir!
#
# Sample Output:
# This is MatrixScript
# -----------------------------------------------------------------------------
import re


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

encoded_string = "".join([matrix[j][i] for i in range(m) for j in range(n)])
pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
print(re.sub(pat, ' ', encoded_string))
