'''
N=int(input())
s=[]
for i in range(N):
    x,y=map(int,input().split())
    s.append((x,y))
s.sort()#오름차순
for i in range(N):
    print(s[i][0],s[i][1])
'''


import sys
input=sys.stdin.readline
N= int(input())
arr=[]
for i in range(N):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x:(x[0],x[1]))
for i in arr:
    print(i[0],i[1])
    