"""Solution for hacker rank iterators and iterables """
# --------------------------------------------------------------
# You are given a list of N lowercase English letters. For a given integer K,
# you can select any K indices(assume -1 based indexing) with
# a uniform probability from the list.
# Find the probability that at least one of the K indices selected will
# contain the letter: 'a'.

# Input Format
# The input consists of three lines. The first line contains the integer N,
# denoting the length of the list.
# The next line consists of N space-separated lowercase English letters,
# denoting the elements of the list.
# The third and the last line of input contains the integer K,
# denoting the number of indices to be selected.
# Note: The answer must be correct up to 3 decimal places.
#--------------------------------------------------------------
import itertools
count_a = 0

# Read Integer N Count of list1
N = int(input())
# Read N letters from input
letters = input().split()
# Read Integer K
K = int(input())
# Create all K indices of letters
all_possible_indices = list(itertools.combinations(letters, K))
# Create a list of indices that contain the letter 'a'
for  elements in all_possible_indices:
    if "a" in elements:
        count_a += 1
# Calculate the probability of the letter 'a'
probability = count_a / len(all_possible_indices)

# print the probability 3 decimal places
print("{:.3f}".format(probability))



