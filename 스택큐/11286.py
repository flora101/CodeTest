import sys
input = sys.stdin.readline
import heapq

n=int(input())
q=[]
for i in range(n):
    a = int(input())
    if a ==0:
        if len(q)==0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q,[abs(a),a])
    
# print(q)
