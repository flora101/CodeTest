import sys
import heapq
input = sys.stdin.readline
q =[]
n=int(input())
for i in range(n):
    a= int(input())
    if a == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, a)
