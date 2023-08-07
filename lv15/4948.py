import sys
input=sys.stdin.readline
def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

while True:
    n=int(input())
    if n==0:
        break
    cnt=0
    for i in range(n+1,2*n+1):
        if check(i)==True:
            cnt+=1
    print(cnt)