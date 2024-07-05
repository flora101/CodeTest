import sys
input = sys.stdin.readline

n, s = map(int, input().split())
num = list(map(int, input().split()))

left = 0
right = 0
cnt = 1e9
temp = num[0]

while right < n:
    if temp >= s:
        cnt = min(cnt, right - left + 1)
        temp -= num[left]
        left += 1
    else:
        right += 1
        if right < n:
            temp += num[right]

if cnt == 1e9:
    print(0)
else:
    print(cnt)
