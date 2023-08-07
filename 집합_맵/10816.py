n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
d={}
for i in arr1:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in arr2:
    result=d.get(i)
    if result==None:
        print(0,end=" ")
    else:
        print(result,end=" ")

#counter 쓰기,dictionary 
# import sys
# from collections import Counter

# M=int(sys.stdin.readline())
# list1=list(map(int,sys.stdin.readline().split()))
# N=int(sys.stdin.readline())
# list2=list(map(int,sys.stdin.readline().split()))

# c= Counter(list1)

# for i in list2:
#   if i in c:
#     print(c[i], end=' ')
#   else:
#     print(0, end=' ')