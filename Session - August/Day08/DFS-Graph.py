#DFS - STACK
graph = {
  '10' : ['2','4','6','8'],
  '2' : ['3', '5'],
  '3' : ['7'],
  '7' : [],
  '5' : ['9'],
  '9':[],
  '4' : ['1'],
  '1' :[],
  '6':['11'],
  '11':[],
'8':[],
}
traversed = set()
def dfs(traversed, graph, vertex):
    if vertex not in traversed:
        print (vertex)
        traversed.add(vertex)
        #print(traversed)
        #print(graph[vertex])
        for adjacent in graph[vertex]:
            dfs(traversed, graph, adjacent)
print("Depth First Search:")
dfs(traversed, graph, '10')










#https://www.delftstack.com/howto/python/dfs-python/







