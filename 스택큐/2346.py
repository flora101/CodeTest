import sys
input=sys.stdin.readline
from collections import deque

n=int(input())
queue=deque(enumerate(map(int,input().split())))
ans=[]

while queue:
    idx,p=queue.popleft() #젤 첫번째꺼는 무조건 빼줌
    ans.append(idx+1)
    
    if p>0:
        queue.rotate(-p+1)
    elif p<0:
        queue.rotate(-p)
for j in ans:
    print(j, end = ' ')
#
