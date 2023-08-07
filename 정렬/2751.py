n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
arr.sort()#오름차순
print(*arr,sep="\n")
