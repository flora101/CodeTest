import sys
input=sys.stdin.readline
m,n=map(int,input().split())

def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for i in range(m,n+1):
    if check(i)==True and i!=1:
        print(i)
