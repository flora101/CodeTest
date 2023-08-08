n=int(input())
arr=list(map(int,input().split()))
arr.sort()
#print(arr)
if n==1:
    print(arr[0]*arr[0])
else:
    print(arr[0]*arr[-1])
