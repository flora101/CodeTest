minus= input().split('-')
num=[]
for i in minus:
    s=0
    add= i.split('+')
    for j in add:
        s+=int(j)
    num.append(s)
ans= num[0]
for i in range(1,len(num)):
    ans-=num[i]
print(ans)