n,k=map(int,input().split())
def fac(a):
    if a<=1:
        return 1
    return a*fac(a-1)
print(fac(n)//(fac(k)*fac(n-k)))
#
