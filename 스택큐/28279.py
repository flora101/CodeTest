from collections import deque
import sys
input=sys.stdin.readline

queue=deque()
n=int(input())

for i in range(n):
    hu = list(map(int,input().split()))
    if hu[0]==6:
        if len(queue)==0:
            print("1")
        else:
            print("0")
    elif hu[0]==1:
        queue.appendleft(hu[1])
    elif hu[0]==2:
        queue.append(hu[1])
    elif hu[0]==3:
        if len(queue)!=0:
            print(queue.popleft())
        else:
            print("-1")
    elif hu[0]==4:
        if len(queue)!=0:
            print(queue.pop())
        else:
            print("-1")
    elif hu[0]==7:
        if len(queue)!=0:
            print(queue[0])
        else:
            print("-1")
    elif hu[0]==8:
        if len(queue)!=0:
            print(queue[-1])
        else:
            print("-1")
    elif hu[0]==6:
        if len(queue)!=0:
            print("0")
        else:
            print("1")
    elif hu[0]==5:
        print(len(queue))