n,m=map(int,input().split())
s=[]

def DFS(start):
    if len(s)==m:
        print(*s)
        return 
    for i in range(start,n+1):
        s.append(i)
        DFS(i)
        s.pop()

DFS(1)
