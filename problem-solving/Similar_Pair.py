#!/bin/python3

# import os
# Complete the 'similarPair' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. 2D_INTEGER_ARRAY edges
#

# Graph Class
from typing import no_type_check_decorator


class Graph:
    """Create Graph from edges list"""
    def __init__(self, n, edges):
        self.size = n

        # Create adjacency list
        self.adj_list = {}

        # Add edges to adjacency adj_list
        for edge in edges:
            if edge[0] not in self.adj_list:
                self.adj_list[edge[0]] = [edge[1]]
            else:
                self.adj_list[edge[0]].append(edge[1])


# Find Root Node of graph
def find_root(adj_list: dict):
    """Find root node of Graph."""

    # Find all nodes
    non_root_nodes = set()

    for node in adj_list:
        for edge in adj_list[node]:
            non_root_nodes.add(edge)

    # Find root Node
    for node in adj_list.keys():
        if node not in non_root_nodes:
            return node


def similarPair(n, k, edges):
    """Write your code here."""

    # Create Graph
    graph = Graph(n, edges)

    # Find root nodes
    root = find_root(graph.adj_list)

    # Print adjacency list and root nodes
    print("adjacency :", graph.adj_list)
    print("root :", root)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = similarPair(n, k, edges)

    # print(result)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
