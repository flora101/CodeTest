import sys
input=sys.stdin.readline
def gcd(x,y):
    if y==0:
        return x
    else:
        return gcd(y,x%y)
    
n=int(input())
arr=[]
arr2=[]
for i in range(n):
    a=int(input())
    arr.append(a)
#print(arr) #나무
for i in range(n-1):
    arr2.append(arr[i+1]-arr[i])
#print(arr2) #간격들
g=arr2[0]
for i in range(len(arr2)-1):
    g=gcd(g,arr2[i+1])
#print(g) #최대공약수
print((max(arr)-min(arr))//g+1-n)