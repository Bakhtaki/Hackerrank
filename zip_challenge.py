"""Zip Challenge HackerRank."""
# The National University conducts an examination of N students in X subjects.
# Your task is to compute the average scores of each student.
#
# Average score  = Sum of the scores Obtained in all subjects by a student
# / Total Number of subjects
#
# Input Format
# The first line contains the integer N and X separated by a space.
# The Next X lines contain the space separated marks obtained by students in a particular subject.
#
# Constraints
# 0 < N < 100
# 0 < X < 100
# Output Format
# Print the average of all students on separate lines.
# The average score must be correct up to 1 decimal place.
# -----------------------------------------------------------------------------
# Read Number of students and subjects
N, X = map(int, input().split())

all_subjects = []

for _ in range(X):
    # Read Marks for Each Subject
    subject = list(input().split())
    all_subjects.append(subject)

student_marks = list(zip(*all_subjects))

for student in student_marks:
    # Average student marks
    marks_average = sum(map(float, student)) / len(student)
    print(round(marks_average, 1))
