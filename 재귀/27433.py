def fac(k):
    if k<=1:
        return 1
    else:
        return (k*fac(k-1))
    
n=int(input())
print(fac(n))