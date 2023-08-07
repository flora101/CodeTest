s=str(input())
res=set()
for i in range(len(s)):
    for j in range(len(s)-i):
        res.add(s[i:j+i+1])
print(len(res))
#