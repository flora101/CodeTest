n=int(input())
num=map(int,input().split())
cnt=0
for i in num:
    arr=[]
    for j in range(i):
        if i % (j+1)==0:
            arr.append(j+1)
    if len(arr)==2:
        cnt+=1
print(cnt)
