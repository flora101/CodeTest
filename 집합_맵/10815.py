n=int(input())
arr1=list(map(int,input().rstrip().split()))
m=int(input())
arr2=list(map(int,input().rstrip().split()))
dic={}
for i in range(n):
    dic[arr1[i]]=0
for i in range(m):
    if arr2[i] not in dic:
        print("0",end=" ")
    else:
        print("1",end=" ")
#