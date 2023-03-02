#Graph is a non linear data structure where it contains nodes or vertices connected theough edges or arcs
#Where set of nodes & set of edges combine to used as represent graphs.
#Types: Finite, Infinite: Ref: https://www.geeksforgeeks.org/graph-types-and-applications/
#Complete Graph n Vetices & n-1 Nodes, one vertex attached to another. --- Full Graph
#Regular graph: All number of vertices == Degree
#Representation: Adjacant matrix & Adjacent List.
#Adjacant matrix is a 2D Array which size v*v.
#In case of directed graphs if there is edge between vI to vJ, we assign Graph of IJ as 1.
#In case of undirected graphts we have to show there is a edge from i to j & Vice Versa.
print('Graphssszzzz')

#BFS and DFS:
#BFS: Breadth First Search
#DFS: Depth First Search
#BFS: It is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node). You must then move towards the next-level neighbour nodes.
#DFS: It is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph until you find the desired node or the node which does not have any child node. The basic idea is to start from the source node and keep exploring the adjacent nodes (nodes which are directly connected to source node). If you reach a node which does not have any adjacent node then backtrack and check for other nodes. Finally, print the nodes in the path.
#BFS: Ref: https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
#DFS: Ref: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/