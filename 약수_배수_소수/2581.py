m=int(input())
n=int(input())
arr=[]
for i in range(m,n+1):
    cnt=0
    for j in range(i):
        if i%(j+1)==0:
            cnt+=1
        if cnt>2:
            break#시간 초과 돼서 추가함 똑똑이!!
    if cnt==2:
        arr.append(i)
if len(arr)==0:
    print("-1")
else:
    print(sum(arr))
    print(arr[0])
