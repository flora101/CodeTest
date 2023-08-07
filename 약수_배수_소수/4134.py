import sys
input=sys.stdin.readline
N=int(input())

def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for i in range(N):
    n=int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if check(n):
            print(n)
            break
        else:
            n+=1
#정수론의 개념인 "임의의 양수 A가 합성수이면 √A 보다 작거나 같은 약수를 가진다." 를 활용