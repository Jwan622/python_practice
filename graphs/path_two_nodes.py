"""
How to Find a Path Between a Source and a Destination
Now that we've seen how to use DFS and BFS to traverse the entire graph and print out the whole traversal history, we can make some small changes to the templates to find a path between any two nodes in the graph (if such path exists).

On a graph where each edge has the same weight, BFS is equivalent to Dijkstra's Shortest Path Algorithm. It finds the shortest path (path with the fewest number of nodes) between a source node and a destination node. This is a nice property that a path search with DFS doesn't have.

Here's how we adapt the DFS template to return a path given a src and a dst node:
"""
from collections import deque


graph = {
    0: [1, 4], # right side are neighbors
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}


def dfs_path(graph, src, dst):
    stack = [(src, [src])]  # the right side of the tuple in the list is the path
    visited = set()
    while stack:
        node, path = stack.pop()  # the pop pop's the neighbor which was just put on the stack
        print('node, path', node, path)
        if node in visited:
            print('node in visited: ', node)
            continue
        if node == dst:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            stack.append((neighbor, path + [neighbor]))
    return None


def bfs_path(graph, src, dst):
  visited, queue = set(), deque([[src]])
  while queue:
    path = queue.popleft()
    node = path[-1]
    if node in visited:
      continue
    if node == dst:
      return path
    for neighbor in graph[node]:
      queue.append(path + [neighbor])
  return None


print(dfs_path(graph, 0, 2))
print(bfs_path(graph, 0, 2))
