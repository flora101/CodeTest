from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip())))
# print(graph)

result = []

def bfs(graph,a,b):
    q = deque()
    q.append([a,b])
    graph[a][b] = 0
    cnt = 1
    while q:
        x,y = q.popleft()
        # graph[x][y]=0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=len(graph) or ny>=len(graph):
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=0
                q.append([nx,ny])
                cnt+=1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            cnt = bfs(graph,i,j)
            result.append(cnt)
            
result.sort()
print(len(result))
for i in result:
    print(i)
    
