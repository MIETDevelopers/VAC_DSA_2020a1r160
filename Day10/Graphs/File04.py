#BFS using recursion
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {}
        for v in vertices:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def BFS(self, queue, visited):
        if not queue:
            return
        curr_node = queue.pop(0)
        print(curr_node, end=" -> ")
        visited.add(curr_node)
        for adj_node in self.adj_list[curr_node]:
            if adj_node not in visited:
                queue.append(adj_node)
                visited.add(adj_node)
        self.BFS(queue, visited)

    def BFS_traversal(self, start_node):
        queue = []
        visited = set()
        queue.append(start_node)
        visited.add(start_node)
        self.BFS(queue, visited)

g = Graph([1, 2, 3, 4, 5])
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.BFS_traversal(1)