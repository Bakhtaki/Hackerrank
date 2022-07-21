"""Calculate average Marks From a list of tuples"""

# ---------------------------------------------------------------

# Task:
# Calculate the average of the marks of all students
#
# Note:
# Colmns can be in any order
# Column namesm spellings,and case wont change

# Input format:
# The First lin contains an integer N, number of students
# The Second line contain names of columns in any order
# The Next N lines contain the marks of students in the
# same order as the names in the second line

# Constraints:
# 1 <= N <= 100

# Output format:
# Print the average of the marks of all students in 2 decimal places

# Sample Input:
# 3
# Name Marks ID class
# Abcdefghi 1001 1 1
# Xyzijklm 1002 2 2
# Pqrstuvw 1003 3 3

# Sample Output:
# 3.33

# ---------------------------------------------------------------

# Solution:

# Import the necessary modules
from collections import namedtuple

# Read the number of students
n = int(input())

# Read the column names
column_names = input().split()

# Create a namedtuple for the students
Student = namedtuple('Student', column_names)

# Read the marks of the students
students = [Student(*input().split()) for _ in range(n)]

# Calculate the average of the marks of all students
average = sum([int(student.MARKS) for student in students]) / n

# Print the average of the marks of all students in 2 decimal places
print("{:.2f}".format(average))

