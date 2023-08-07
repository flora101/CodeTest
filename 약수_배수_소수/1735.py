def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)

a,b=map(int,input().split())
c,d=map(int,input().split())

r=gcd((a*d+b*c),(b*d))
#print(r)
print((a*d+b*c)//r,(b*d)//r)