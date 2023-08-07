arr=[]
arr2=[]
for _ in range(3):
    a,b=map(int,input().split())
    arr.append(a)
    arr2.append(b)
print(sum(set(arr))*2-sum(arr),sum(set(arr2))*2-sum(arr2))