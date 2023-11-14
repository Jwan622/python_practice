"""
detect cycle:
Detect Cycle in a Directed Graph using DFS:
The problem can be solved based on the following idea:

To find cycle in a directed graph we can use the Depth First Traversal (DFS) technique. It is based on the idea that
there is a cycle in a graph only if there is a back edge [i.e., a node points to one of its ancestors] present in the graph.

To detect a back edge, we need to keep track of the nodes visited till now and the nodes that are in the current
recursion stack [i.e., the current path that we are visiting]. If during recursion, we reach a node that is already
in the recursion stack, there is a cycle present in the graph.


If the graph is disconnected then get the DFS forest and check for a cycle in individual trees by checking back edges.

Follow the below steps to Implement the idea:

Create a recursive dfs function that has the following parameters – current vertex, visited array, and recursion stack.
Mark the current node as visited and also mark the index in the recursion stack.
Iterate a loop for all the vertices and for each vertex, call the recursive function if it is not yet visited (This step is done to make sure that if there is a forest of graphs, we are checking each forest):
In each recursion call, Find all the adjacent vertices of the current vertex which are not visited:
If an adjacent vertex is already marked in the recursion stack then return true.
Otherwise, call the recursive function for that adjacent vertex.
While returning from the recursion call, unmark the current node from the recursion stack, to represent that the current node is no longer a part of the path being traced.
If any of the functions returns true, stop the future function calls and return true as the answer.

"""
from collections import defaultdict


class Graph():
	def __init__(self, vertices_count):
		self.graph = defaultdict(list)
		self.vertices_count = vertices_count

	def add_node(self, root_node, new_node):
		self.graph[root_node].append(new_node)

	def is_cycle_helper(self, node, visited, rec_stack):
		visited[node] = True
		rec_stack[node] = True
		print('visited in cycle helper: ', visited)
		print('rec_stack in cycle helper: ', rec_stack)
		# if any neighbour is visited and in recStack then graph is cyclic
		for neighbour in self.graph[node]:
			print('neighbor: ', neighbour)
			if visited[neighbour] is False:
				if self.is_cycle_helper(neighbour, visited, rec_stack) is True:
					print('is in is_cycle_helper is True clause', neighbour)
					return True
			elif rec_stack[neighbour] is True:  # if we get here, then the neighbour is in visited True and is in rec_stack too,
				# then cycle. remember the rec_stack represents the current path that we are visiting
				print('in rec_stack[neighbour] is True clause', neighbour)
				return True

		print('we start popping nodes')
		rec_stack[node] = False
		return False

	# Returns true if graph is cyclic else false
	def is_cyclic(self):
		visited = [False] * (self.vertices_count + 1)
		rec_stack = [False] * (self.vertices_count + 1)
		print('visited at beginning: ', visited)
		print('rec_stack at beginning: ', rec_stack)
		for node in range(self.vertices_count):  # not inclusive of the count number... gonna be 1 less. we also start at 0
			print('node in is_cyclic: ', node)
			if visited[node] is False:
				if self.is_cycle_helper(node, visited, rec_stack) is True:
					return True
		return False


if __name__ == '__main__':
	g = Graph(4)
	g.add_node(0, 1)
	g.add_node(0, 2)
	g.add_node(1, 2)
	g.add_node(2, 0)
	g.add_node(2, 3)
	g.add_node(3, 3)
	print('graph: ', g.graph)
	if g.is_cyclic() == 1:
		print("Graph contains cycle")
	else:
		print("Graph doesn't contain cycle")
