#Depth First Search on a undirected graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def addEdge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def DFS(self, v, visited = [False]*5):
        visited[v] = True
        print(v, end=' -> ')
        for i in range(self.V):
            if self.graph[v][i] == 1 and visited[i] == False:
                self.DFS(i, visited)
g = Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,2)
g.addEdge(2,4)
g.addEdge(3,4)
g.DFS(0)