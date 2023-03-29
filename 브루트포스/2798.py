N,M=map(int,input().split())
s= list(map(int,input().split()))
result=0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if s[i]+s[j]+s[k]>M:
                continue
            else:
                result=max(result,s[i]+s[j]+s[k])
print(result)