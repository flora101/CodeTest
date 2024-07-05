from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for i in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(v):
    global cnt
    q= deque([v])
    visited[v] =1
    while q:
        a = q.popleft()
        graph[a].sort()
        for i in graph[a]:
            if visited[i]==0:
                cnt+=1
                visited[i] = cnt
                q.append(i)
                
bfs(r)

for v in range(1, n+1):
    print(visited[v])
                
