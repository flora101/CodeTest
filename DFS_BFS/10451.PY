import sys
sys.setrecursionlimit(10**7)
T= int(input())

def dfs(v):
    visited[v]=1
    next= data[v]
    if visited[next]==0:
        dfs(next)
    

for _ in range(T):
    N= int(input())
    data = [0]+list(map(int,input().split()))
    visited= [0]*(N+1)
    ans=0
    for i in range(1,N+1):
        if visited[i]==0:
            dfs(i)
            ans+=1
    print(ans)