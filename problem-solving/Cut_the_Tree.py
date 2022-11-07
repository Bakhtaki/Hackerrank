"""Hacker Rank - Algorithms - Graph Theory - Cut the Tree."""
import os

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges


# Define functio to calculate the minimum difference of the tree
def min_diff(graph, start, wights):
    """Calculate the minimum difference of two subtree."""
    total_wight = sum(wights)

    # Define Stack
    stack = [start]

    # Define visited nodes
    visited = set()

    # Initialize the minimum difference
    min_diff = [float('inf')]

    # Save the wights of the nodes
    node_wights = dict()

    # Save Nodes and Parents
    child_parent = dict()

    # DFS to find the minimum difference
    while stack:
        vertex = stack[-1]

        if vertex in visited:
            # Cumulative sum of the node is the sum of the node and the sum of
            # the children
            node_wights[vertex] = wights[vertex-1]
            for child in graph[vertex]:
                if child in child_parent.get(child, -1) == vertex:
                    node_wights[vertex] += node_wights[child]
            # Calculate the difference
            min_diff[0] = min(min_diff[0],
                              abs(total_wight - 2 * node_wights[vertex]))
            stack.pop()
            continue
        else:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
                    child_parent[neighbor] = vertex
    return min_diff


# Create a graph with the edges
def create_graph(nodes, edges):
    """Create a graph with the edges."""
    graph = dict()

    for _start, _end in edges:
        if _start not in graph.keys():
            graph[_start] = [_end]
        else:
            graph[_start].append(_end)

        if _end not in graph.keys():
            graph[_end] = [_start]
        else:
            graph[_end].append(_start)
    # Update the graph with the nodes
    graph.update({k: [] for k in range(1, nodes+1) if k not in graph.keys()})
    return graph


def cutTheTree(data, edges):
    """Write your code here."""
    graph = create_graph(len(data), edges)
    return min_diff(graph, 1, data)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
