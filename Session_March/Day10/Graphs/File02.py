class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None]*vertices
    def addEdge(self, src, des):
        node=Node(des)
        node.next=self.graph[src]
        self.graph[src]=node

        node=Node(src)
        node.next=self.graph[des]
        self.graph[des]=node
    def printGraph(self):
        for i in range(self.V):
            print("The adjacent list: ", i+1)
            temp = self.graph[i]
            while temp:
                print(temp.vertex, end="->")
                temp = temp.next
            print()
        
graph=Graph(5)
graph.addEdge(0,1)
graph.addEdge(1,4)
graph.addEdge(1,3)
graph.addEdge(2,0)
graph.addEdge(2,3)
graph.addEdge(3,4)
graph.printGraph()