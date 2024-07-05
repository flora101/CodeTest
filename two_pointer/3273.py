import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
x = int(input())
cnt = 0

num.sort()
# print(num)

a,b = 0,n-1
while a<b:
    temp = num[a]+num[b]
    if temp == x:
        cnt+=1
        a+=1
    elif temp < x:
        a+=1
    else:
        b-=1
print(cnt)
