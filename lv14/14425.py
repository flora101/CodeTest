# n,m=map(int,input().split())
# cnt=0
# for _ in range(n):
#     s=set(input())
# for i in range(m):
#     c=input()
#     if c in s:
#         cnt+=1
# print(cnt)

n,m=map(int,input().split())
a={}
cnt=0
for _ in range(n):
    s=input()
    a[s]=True
for _ in range(m):
    s1=input()
    if s1 in a.keys():
        cnt+=1

print(cnt)
#
#딕셔너리, set 어렵다..