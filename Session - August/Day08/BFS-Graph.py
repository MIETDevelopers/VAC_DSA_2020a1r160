graph = {
  'A' : ['B','C','D','E','F'],
  'B' : ['G', 'H'],
  'C' : ['I','J','K'],
  'D' : ['L'],
  'E' : ['M'],
  'F' : [],
  'G':['N'],
  'K':['Z'],
  'H': [],
  'I' :[],
  'J' :[],
  'L' :[],
  'M' :[],
  'N' :[],
  'Z' :[],
}


visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  #print(visited)
  #print(queue)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 
    #print(graph[s])
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'B')


#