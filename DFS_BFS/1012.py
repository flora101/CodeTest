import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph,i,j):
    q = deque()
    q.append([i,j])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=len(graph) or ny>=len(graph[0]):
                continue
            if graph[nx][ny]==1:
                q.append([nx,ny])
                graph[nx][ny]=0


t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [[0 for j in range(m)] for i in range(n)]
    cnt = 0
    for _ in range(k):
        x,y = map(int,input().split())
        graph[y][x] = 1
        
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                bfs(graph,i,j)
                cnt+=1
    print(cnt)
