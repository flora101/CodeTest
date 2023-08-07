from collections import deque
n,k=map(int,input().split())
queue = deque()
ans=[]
for i in range(n):
    queue.append(i+1)
while queue: #for _ in queue: 이렇게 적으면 안됨
    for i in range(k-1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())


print('<', end='')
print(*ans, sep=', ' ,end= '') 
print('>')
#출력 양식 주의 
#