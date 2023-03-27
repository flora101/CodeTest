T= int(input())
for _ in range(T):
    s = list(input().split())
    for i in s:
        print(i[::-1],end= " ")