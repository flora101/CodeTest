import sys
input = sys.stdin.readline

n,m=map(int,input().split())
work = list(map(int,input().split()))

left = 0
right = m
temp = sum(work[left:right])

answer = temp
while right < n:
    temp = temp+work[right]-work[left]
    answer = max(answer,temp)
    left+=1
    right+=1
print(answer)
