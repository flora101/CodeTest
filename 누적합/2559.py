import sys
input = sys.stdin.readline
n,k = map(int,input().split())
temp = list(map(int,input().split()))

for i in range(n-1):
    temp[i+1]+=temp[i]
# print(temp)
temp2=temp[k-1]
right = k
while right<n:
    temp2 = max(temp2, temp[right]-temp[right-k])
    right+=1
print(temp2)
