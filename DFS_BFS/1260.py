from collections import deque
N,M,V=map(int,input().split())
graph=[[]for _ in range(N+1)]

def dfs(v):
    visited[v]=1
    print(v, end=" ")
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)

def bfs(v):
    queue= deque([v])
    visited[v]=1
    while queue:
        v=queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if visited[i]==0:
                visited[i]=1
                queue.append(i)
            
for _ in range(M):
    a,b=list(map(int,input().split()))
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()
    
visited = [0]*(N+1)
dfs(V)
print()

visited = [0]*(N+1)
bfs(V)