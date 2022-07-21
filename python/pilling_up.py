"""Solution for Hacker ranck Pilling Up problem."""

# -----------------------------------------------------------------------------
# There is horizontal row of n cubes. The length of each cube is given.
# You need to create a new vertical pile of cubes.The new pile should
# follow these rules:
# if cube[i]is on top of cube [j], then sideLenght[j] >= sideLength[i]
# The new pile should be strictly larger than the old one.
# when stacking the cubes,You can only pick the leftmost or the rightmost
# cube each time.
# Print Yes if it is possible to create the new pile, otherwise print No.
# Example:
# Block 1: [1,2,3,8,7]
# Result: No
# 
# Block 2: [1,2,3,4,5]
# Result: Yes
# Input Format:
# The first line contains an integer T, the number of test cases.
# foreach test case there is two lines.
# The first line contains an integer n, the number of cubes.
# The second line contains n space separated integers, the length of each cube.
# 
# Constraints:
# 1 <= T <= 5
# 1 <= n <= 10^5
# 1 <= sideLength[i] <= 2^31
#
# Output Format:
# For each test case, output a single line containing either Yes or No.
# 
# Sample Input:
# 2 # number of test cases
# 6 # block [] size n = 6
# 4 3 2 1 3 4 block = [4,3,2,1,3,4]
# 
# 3 # block [] size n = 3
# 1 2 3 block = [1,2,3]
#
# Sample Output:
# Yes
# No
# -----------------------------------------------------------------------------
# Solution:

# Import the necessary modules.
from collections import deque

for _ in range(int(input())):  
    _, queue =input(), deque(map(int, input().split()))
    
    for cube in reversed(sorted(queue)):
        if queue[-1] == cube: queue.pop()
        elif queue[0] == cube: queue.popleft()
        else:
            print('No')
            break
    else: print('Yes')
