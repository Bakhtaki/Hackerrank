"""Calendar Module for the Calendar App."""

# -----------------------------------------------------------------------------
# Task
# You are given a date. Your task is to find what the day is on that date.

# Input Format
# A single line of input containing the space separated values of day,
# month and year respectively in the format dd mm yyyy.

# Constraints
# 2000 <= yyyy <= 3000

# input:
# A single line of input containing the space separated values of day,

# Output Format
# Output the correct day in capital letters.

# Explanation
# the day on 5 Augusts 2015 was "Wednesday"

# Sample Input
# 05 08 2015

# Sample Output
# Wednesday
# -----------------------------------------------------------------------------

# Import the calendar module.
import calendar

# Read input
month, day, year = map(int, input().split())

# Define name of the day.
day_name = calendar.day_name[calendar.weekday(year, month, day)]

# Print the day name in Capital Letters
print(day_name.upper())
