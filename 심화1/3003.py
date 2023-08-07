arr=list(map(int,input().split()))#일렬로 할때는 요렇게!!
ch=[1,1,2,2,2,8]
for i in range(6):
    ch[i]-=arr[i]
print(*ch)