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


print('dfs: ', dfs(graph, 2))