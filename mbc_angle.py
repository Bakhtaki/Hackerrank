"""Find MBC angle in triangular lattice."""
# -----------------------------------------------------------------------------
# ABC in Triangle ,90 degree angle in B
# Point M is in the middle of the triangle
# You are given AB , BC
# You need to find the MBC angle

# Input format:
# The first line contains the length of AB
# The second line contains the length of BC
#
# Constraints:
# 0 < AB < 100
# 0 < BC < 100
#
# Output format:
# The output is the angle MBC in degrees
# Note: Round the answer to the nearest integer
# Example:
# if angle is 60.5 then output is 61
# if angle is 57.888 then output is 58
#
# Sample Input:
# 10
# 10
# Sample Output:
# 45
# -----------------------------------------------------------------------------
import math

# Read AB and BC
AB = int(input())
BC = int(input())

# Calculate AC
AC = math.hypot(AB, BC)

# Calculate angle MBC
MBC = math.degrees(math.acos(BC/AC))

# Print angle MBC
print(round(MBC),chr(176),sep='')