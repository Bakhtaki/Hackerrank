"""Set Operations"""
# ---------------------------------------------------------------
# Task
# ---------------------------------------------------------------
# You have a non-empty set S,and you have to execute N commands
# given in N lines.
# The commands are as follows:
# pop, remove, discard.
#
# Input Format
# The first line contains integer n, the number of elements in the set S.
# The second line contains n space separated elements of set S.
# The third line contains integer N, the number of commands.
# The next N lines contains commands to execute on set S.
#
# Output Format
# Print the sum of all elements of set S on a single line.

# Constraints
# 0 < N < 20
# 0 < n < 20
#
# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 12
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# Sagample Output
# 5
# ---------------------------------------------------------------
# Solution
# Read the input from the console
n = int(input())
s = set(map(int, input().split()))
n_commands = int(input())

for _ in range(n_commands):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

# Print the sum of all elements of set S on a single line.
print(sum(s))
