"""
Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree (See method 2 of this post).
The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid
processing a node more than once, we use a boolean visited array. For simplicity, it is assumed that all vertices are
reachable from the starting vertex.

For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0, we look for all adjacent
vertices of it. 2 is also an adjacent vertex of 0. If we don’t mark visited vertices, then 2 will be processed again and
it will become a non-terminating process. A Breadth First Traversal of the following graph is 2, 0, 3, 1.
"""
# Python3 Program to print bfs traversal from a given source vertex. bfs(int root_node)
from collections import defaultdict


# This class represents a directed graph
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
		self.visited = []

	# function to add an edge to graph. Make a list visited[] to check if a node is already visited or not
	def add_node(self, root_node, new_node):
		print('root node: ', root_node)
		print('new node: ', new_node)
		self.graph[root_node].append(new_node)

	def bfs(self, s):
		queue = []  # this allows us to do breadth first

		queue.append(s)
		self.visited.append(s)
		while queue:
			s = queue.pop(0)

			for node in self.graph[s]:
				if node not in self.visited:
					queue.append(node) # so we add the node's sister nodes to the queue and then pop the next round.
					self.visited.append(node)

		print('visited: ', self.visited)


if __name__ == "__main__":
	g = Graph()
	g.add_node(0, 1)
	g.add_node(0, 2)
	g.add_node(1, 2)
	g.add_node(2, 0)
	g.add_node(2, 3)
	g.add_node(3, 3)

	print("Following is Breadth First Traversal (starting from vertex 2)")
	g.bfs(2)
