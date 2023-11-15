graph = {
    0: [1, 4], # right side are neighbors
    1: [0, 2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [0, 1, 3]
}


def dfs(graph, start):
	visited, stack = set(), [start]

	while stack:
		node = stack.pop()
		if not node in visited:
			print('Now visiting', node)
		visited.add(node)
		for neighbor in graph[node]:
			if not neighbor in visited: # since this is depth first search (dfs), we stack the neighbors on top of the stack and then we pop it off and add it to vistitor on the next loop before going back to original node's neighbors
				print('neighbor', neighbor)
				stack.append(neighbor)
	return visited

'''
How to Use Depth-First Search
As its name suggests, dfs prioritizes depth in its search.

For a given node (say 1), after visiting one of its neighbors (say 0), instead of visiting the rest of the neighbors (nodes 2, 3, and 4) immediately, it caches those neighbors and immediately resumes its visit on 0's neighbors.
'''
# print('dfs: ', dfs(graph, 2))

from collections import deque as dequePython


# now let's checkout breadth first.
def bfs(graph, start):
	visited, deque = set(), dequePython([start])

	while deque:
		node = deque.popleft()  # we popleft instead of pop for bfs so we visit all of the first node's neighbors first, which is breadth
		if not node in visited:
			print('Now visiting', node)
		visited.add(node)  # this keeps track of the order of visits
		for neighbor in graph[node]:
			if not neighbor in visited:
				print('neighbor: ', neighbor)
				deque.append(neighbor) # append is at the end for deque
	return visited

print('bfs: ', bfs(graph, 0))

# Python3 program to print dfs traversal
# from a given graph
from collections import defaultdict


# This class represents a directed graph.
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_node(self, root, new_node):
		print('root: ', root)
		print('new node: ', new_node)
		self.graph[root].append(new_node)

	def dfs_helper(self, node, visited):
		visited.add(node)
		print(node, end=' ')

		for neighbour in self.graph[node]:
			if neighbour not in visited:
				self.dfs_helper(neighbour, visited)

	def dfs(self, root_node):
		visited = set()
		self.dfs_helper(root_node, visited)

'''
Time Complexity: O(V+E) where V is the number of vertices in the graph and E is the number of edges
Auxiliary Space: O(V+E)
'''
if __name__ == "__main__":
	g = Graph()
	g.add_node(0, 1)
	g.add_node(0, 2)
	g.add_node(1, 2)
	g.add_node(2, 0)
	g.add_node(2, 3)
	g.add_node(3, 3)

	print("Following is Depth First Traversal (starting from vertex 2)")
	g.dfs(2) # this goes all the way to 1 first before going breadth to 3
