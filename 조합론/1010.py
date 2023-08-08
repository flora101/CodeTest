def fac(r):
    if r<=1:
        return 1
    return r*fac(r-1)

t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    print(fac(b)//(fac(a)*fac(b-a))) 
