#!/bin/python3

import os
from collections import defaultdict


#
# Complete the 'letterIslands' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
# Define Custom Suffix Tree Class
class SuffixTree:
    def __init__(self, string, k):
        """Initializes the SuffixTree class."""
        self.string = string
        self.string_length = len(string)
        self.k = k
        self.result = 0

    def get_substring_indexes(self):
        """Returns a list of all the indexes of the substring in the string"""

        cache = defaultdict(list)
        for (index, letter) in enumerate(self.string):
            cache[letter].append(index)

        for (_, value) in cache.items():
            len_value = len(value)
            if len_value < self.k:
                continue
            for i in range(len(value) - 1):
                if value[i + 1] - value[i] == 1:
                    len_value -= 1
                if len_value == self.k:
                    self.result += 1
        return cache

    def get_result(self):
        """Returns the result of the algorithm."""
        for (let, pos) in self.get_substring_indexes().items():
            len_ = 1
            arr = [[let, pos]]

            while len(arr) > 0:
                dict_ = defaultdict(list)
                temp = []
                for each in arr:
                    for indices in each[1]:
                        try:
                            dict_[each[0] + self.string[indices +
                                                        len_]].append(indices)
                        except IndexError:
                            pass
                len_ += 1
                for (_, value) in dict_.items():
                    l = len(value)
                    if l < self.k:
                        continue
                    i = 0
                    len_val = len(value)

                    while l < self.k and i < len_val - 1:
                        if value[i + 1] - value[i] == len_:
                            l -= 1
                        i += 1
                    if l == self.k:
                        self.result += 1
                    if l > self.k - 1:
                        temp.append([_, value])
                arr = temp
        return self.result


def letterIslands(s, k):
    """Write your code here."""
    # Create a suffix Tree
    suffix_tree = SuffixTree(s, k)

    # Return the get_result() method of the suffix Tree
    return suffix_tree.get_result()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    k = int(input().strip())

    result = letterIslands(s, k)

    fptr.write(str(result) + '\n')

    fptr.close()
