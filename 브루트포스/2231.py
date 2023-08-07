n=int(input())
for i in range(n+1):
    s=i
    for j in str(i):
        s+=int(j)
    if s == n:
        print(i)
        break
    if i==n:
        print("0")
        break
#