import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline #이거 무조건 해주기

N,M=map(int,input().split())
visited=[0]*(N+1)
graph=[[]for _ in range(N+1)]
cnt=0

def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            dfs(i)

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for j in range(1,N+1):
    if visited[j]==0:
        dfs(j)
        cnt+=1
print(cnt)