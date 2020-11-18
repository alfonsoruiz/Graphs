from collections import deque
from collections import defaultdict

'''
Understand:
Build a graph representing ancestor relationships

Plan:
1. Translate problem into graph terminology
    Vertex - users
    Edges - parent child releationship between two users
    Weights - none
    Paths - users family tree

2. Build graph (if needed)
    Build graph based on edges given, each user has a directed edge to ancestor/parent

3. Traverse graph
    Traverse all paths from starting node, keep track of furthest node found with lowest user id
'''


def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    stack = deque()
    # Node and disctance from starting node
    stack.append((starting_node, 0))
    visited = set()
    earliest_ancestor = (starting_node, 0)

    while len(stack) > 0:
        # Current node, distance from starting node
        curr = stack.pop()
        curr_node, distance = curr[0], curr[1]
        visited.add(curr)

        if curr_node not in graph:
            if distance > earliest_ancestor[1]:
                earliest_ancestor = curr
            elif distance == earliest_ancestor[1] and curr_node < earliest_ancestor[0]:
                earliest_ancestor = curr
        else:
            for ancestor in graph[curr_node]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    return earliest_ancestor[0] if earliest_ancestor[0] != starting_node else -1


def createGraph(edges):
    # Every key added to dict will intialize with a set
    graph = defaultdict(set)

    for edge in edges:
        ancestor, child = edge[0], edge[1]
        # Note: Children are the nodes and ancestors are connections
        graph[child].add(ancestor)

    return graph
