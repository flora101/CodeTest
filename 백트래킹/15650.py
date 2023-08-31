n,m=map(int,input().split())
s=[]
visited=[False] * (n+1) #왜 플러스 일 하냐?
def DFS(start):
    if len(s)==m:
        print(*s)
        return 
    for i in range(start,n+1):
        if visited[i]==True:
            continue
        visited[i]=True
        s.append(i)
        DFS(i+1)
        s.pop()
        visited[i]=False
DFS(1)
