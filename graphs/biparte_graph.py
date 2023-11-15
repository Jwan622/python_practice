from collections import deque
from typing import List


RED = 0
BLUE = 1

"""
A Bipartite Graph is a graph whose vertices can be divided into two independent sets, U and V such that every edge (u, v) either connects a vertex from U to V or a vertex from V to U. In other words, for every edge (u, v), either u belongs to U and v to V, or u belongs to V and v to U. We can also say that there is no edge that connects vertices of same set.
"""
class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return False
        queue, visited = deque([]), set()

        for v in range(len(graph)):
            print('v: ', v)
            if v in visited:
                continue
            queue.append(v)
            node_colors = {v: RED}  # default first node to Red
            print('ndoe_colors: ', node_colors)
            while queue:
                node = queue.popleft()
                print('node popped: ', node)
                visited.add(node)
                my_color = node_colors[node]    # lookup color of node
                for neighbor in graph[node]:
                    if neighbor in node_colors and node_colors[neighbor] == my_color:   # basically if we visited the neighbor already and it's the same color, then not bipartite. in a bipartite graph, no nodes in the same set are connected to each other.
                        print('not bipartite', neighbor, node_colors, my_color)
                        return False
                    if not neighbor in visited:
                        queue.append(neighbor)
                    node_colors[neighbor] = RED if my_color == BLUE else BLUE

        return True


name = 1
test_dict = {name: 'red'}
print(test_dict[name])


graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]

s = Solution()
s.is_bipartite(graph)
