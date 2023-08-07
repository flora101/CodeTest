#2 제곱, 3제곱, 5제곱, 9 제곱, 5곱하기 2-1의 제곱
n=int(input())
p=3
for i in range(n-1):
    if n==1:
        p=3
    else:
        p=p*2-1
#print(p)
print(p**2)