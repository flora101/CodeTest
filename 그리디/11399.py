N = int(input())
time = list(map(int, input().split()))
time.sort()
ans=0
for i in range(N):
    ans += (N-i)*time[i]
print(ans)