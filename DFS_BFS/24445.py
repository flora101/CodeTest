import sys
input = sys.stdin.readline
from collections import deque

n,m,r = map(int,input().split())
graph =[[] for i in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 1

def bfs(v):
    global cnt
    q = deque([v])
    visited[v] = cnt
    while q:
        a = q.popleft()
        graph[a].sort(reverse = True)
        for i in graph[a]:
            if visited[i] == 0:
                cnt+=1
                visited[i] = cnt
                q.append(i)
bfs(r)

for i in range(1,n+1):
    print(visited[i])
