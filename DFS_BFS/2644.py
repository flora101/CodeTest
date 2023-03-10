n= int(input())
a,b= map(int,input().split())
m= int(input())
cnt=0
visited=[0]*(n+1)
graph=[[] for _ in range(n+1)]
res=[0]*(n+1)
def dfs(v):
    visited[v]=1
    for i in graph[v]:
        if visited[i]==0:
            res[i]=res[v]+1
            dfs(i)
    
for _ in range(m):
    x,y= map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
dfs(a)
if res[b]>0:
    print(res[b])
else:
    print(-1)

 