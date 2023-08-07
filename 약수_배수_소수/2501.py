arr=[]
n,k=map(int,input().split())
for i in range(n):
    if n%(i+1)==0:
        arr.append(i+1)
#print(arr)
if len(arr)<k:
    print("0")
else:
    print(arr[k-1])