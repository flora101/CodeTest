x= int(input())
N= int(input())
for i in range(N):
    a,b = map(int,input().split())
    x-=a*b
if x==0:
    print("Yes")
else:
    print("No")