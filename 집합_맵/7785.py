import sys
input = sys.stdin.readline
n=int(input())
d={}
for _ in range(n):
    a,b=input().split()
    if b=='enter':
        d[a]=b
    else:
        del d[a]
ans=d.keys()
for i in sorted(ans,reverse=True):
    print(i)
#