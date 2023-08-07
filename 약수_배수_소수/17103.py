import sys
T=int(input())
N=[0]*T
maxN=0
for i in range(T):#max 구하기
    a=int(sys.stdin.readline())
    N[i]=a
    if maxN<a:
        maxN=a

prime=[True]*(maxN+1)
prime[1]=False
for i in range(2,int(maxN**0.5)+1):
    if prime[i]:
        for j in range(i+i,maxN+1,i):
            prime[j]=False
for i in N:
    ck=0
    for j in range(2,i//2+1):
        if prime[j] and prime[i-j]:
            ck+=1
    print(ck)
#좀 아리까리 모르겠다..
