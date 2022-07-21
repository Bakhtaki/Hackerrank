"""Solution for word order challenge."""
# -----------------------------------------------------------------------------
#
# TASK:
# You are given N words. Some words may repeat.
# For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance
# of the word. See the sample input/output for clarification.
# Note: Each input line ends with a "\n" character.
#
# Constraints:
# 1 <= N <= 10 ^ 5
# The sum of the lengths of all the words do not exceed 10 ^ 6
# All the words are composed of lowercase English letters only.
#
# Input Format:
# The first line contains an integer, N, denoting the number of words.
# The next N lines each contain a word.
#
# Output Format:
# Output 2 lines.
# On the first line, output the number of distinct words from the input.
# On the second line, output the number of occurrences for each distinct word
# according to its input order.
# Sample Input:
# 4
# bcdef
# abcdefg
# bcdef
# bcdef
# Sample Output:
# 3
# 2 1 1
# -----------------------------------------------------------------------------
# Solution:
# -----------------------------------------------------------------------------
# Read input from stdin.
n = int(input())
words = []
for i in range(n):
    words.append(input())

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# Print the number of distinct words.
print(len(word_count))
# Print the number of occurrences for each distinct word.
for word in word_count:
    print(word_count[word], end=" ")

