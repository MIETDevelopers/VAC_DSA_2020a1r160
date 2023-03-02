#Breadth first search
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def add_edge(self, src, dest):
        self.adj[src].append(dest)
    
    def BFS(self, start):
        visited = [False] * self.V
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" -> ")
            for i in self.adj[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,2)
g.add_edge(2,4)
g.add_edge(3,4)
g.BFS(0)