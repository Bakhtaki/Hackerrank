#!/bin/python3

import os
#
# Complete the 'countSubstrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. 2D_INTEGER_ARRAY queries
#

# Define Class Trie


class TrieNode:
    """Structure of TrieNode."""

    def __init__(self, char):
        # Character in the Node
        self.char = char

        # Flag to indicate end of word
        self.end = False

        # Dictionary of Children where key is the
        # character and value is the Node
        self.children = {}

    def __repr__(self):
        return f"{self.children}"


# Define Trie class
class Trie:
    """Trie Struct."""

    def __init__(self):
        """The root Node Should be empty."""
        self.root = TrieNode("")
        self.node_count = 0

    def insert(self, string):
        """Insert a string into the Trie."""
        node = self.root

        # Check each character in the STRING
        # If the character is not in the children of the current node, add it
        # to current node.
        for char in string:
            if char in node.children:
                node = node.children[char]
            else:
                # if the character not found in children,
                # create and# new Trie node
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
                self.node_count += 1
        # Set the end flag to True
        node.end = True

    def search(self, string):
        """Search for a string in the Trie."""
        node = self.root

        # Check each character in the STRING
        # If the character is not in the children of
        # the current node, return False
        # to current node.
        for char in string:
            if char not in node.children:
                return False
            else:
                node = node.children[char]

        # Return True if the end flag is set
        return node.end


def countSubstrings(s, queries):
    # Write your code here
    # Create a TrieNode
    answers = []

    for _q in queries:
        # Get Index Left and Right
        left = _q[0]
        right = _q[1]

        # Get The countSubstring
        substring = s[left:right + 1]
        trie = Trie()
        for i in range(0, len(substring)):
            trie.insert(substring[i:])
        answers.append(trie.node_count)

    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    s = input()

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = countSubstrings(s, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
