arr=[]
arr1=[]
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    arr.append(a)
    arr1.append(b)
print((max(arr)-min(arr))*(max(arr1)-min(arr1)))