# 왜 틀렸지..?
#a,b = map(int, input().split())
# x = 0
# if a == 0:
#     a = a+24
# x = a * 60 + b - 45
# a = x // 60
# b = x % 60
# print(a,b)

a,b = map(int, input().split())
if b >= 45:
    print(a, b-45)
else:
    if a == 0:
        print(a+23, b+15)
    else:
        print(a-1, b+15)