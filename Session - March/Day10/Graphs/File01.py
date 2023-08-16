#Adjacant matrix using graphs.
n,m = map(int, input().split())
graph = [[0 for i in range(n) for j in range(n)]]
for k in range(n):
    i,j = map(int,input().split())
    graph[i-1][j-1]=1
    graph[j-1][i-1]=1
print(graph)