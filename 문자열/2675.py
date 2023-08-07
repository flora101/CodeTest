T=int(input())
for i in range(T):
    r,s=input().split()
    str=''
    for j in range(len(s)):
        str+=s[j]*int(r)
    print(str)