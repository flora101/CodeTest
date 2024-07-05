import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))
num.sort()

left = 0
right = len(num)-1

temp = abs(num[left]+num[right])
final = [num[left],num[right]]

while left < right:
    if abs(num[left]+num[right]) < temp:
        temp = abs(num[left]+num[right])
        final = [num[left],num[right]]
        if temp == 0:
            break
    if num[left]+num[right]<0:
        left+=1
    else:
        right-=1
print(final[0],final[1])
