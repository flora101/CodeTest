from collections import deque
import sys
input=sys.stdin.readline
T=int(input())

for _ in range(T):
    N,M=map(int,input().split())
    queue=deque(list(map(int,input().split())))
    cnt=0
    while queue:
        best=max(queue)
        front=queue.popleft()
        M-=1
        if front==best:
            cnt+=1
            if M<0:
                print(cnt)
                break
        else:
            queue.append(front)
            if M<0:
                M=len(queue)-1