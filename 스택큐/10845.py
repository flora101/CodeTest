from collections import deque
import sys
input=sys.stdin.readline
N=int(input())
queue= deque()
for _ in range(N):
    x=input().split()
    if x[0]=="push":
        queue.append(x[1])
    elif x[0]=="pop":
        if not queue:
            print("-1")
        else:
            print(queue.popleft())
    elif x[0]=="size":
        print(len(queue))
    elif x[0]=="empty":
        if not queue:
            print("1")
        else:
            print("0")
    elif x[0]=="front":
        if not queue:
            print("-1")
        else:
            print(queue[0])
    elif x[0]=="back":
        if not queue:
            print("-1")
        else:
            print(queue[-1])