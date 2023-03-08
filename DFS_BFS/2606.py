cnt=0
N=int(input())
T= int(input())
visited=[0]*(N+1)
graph=[[]for _ in range(N+1)]

def dfs(v):
    global cnt
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)
            cnt+=1
    
for _ in range(T):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs(1)
print(cnt)