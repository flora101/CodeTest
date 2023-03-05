N = int(input())
time=[]
for _ in range(N):
    a,b= map(int, input().split())
    time.append([a,b])
time= sorted(time,key=lambda x: x[0])
time= sorted(time,key=lambda x: x[1])
last=0
cnt=0
for i,j in time:
    if i >= last:
        cnt+= 1
        last = j
print(cnt)