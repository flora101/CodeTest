# n=int(input())
# c=0
# for i in range(1,n+1):
#     cnt=0
#     for j in range(1,i+1):
#         if i % j==0:
#             cnt+=1
#     if cnt%2!=0:
#         c+=1
# print(c)
#약수 개수 구해서 하는 풀이 -> 시간초과 뜸

n = int(input())
cnt = 0
for i in range(1, n+1):
    if i**2 <= n:
        cnt += 1
    else:
        break
print(cnt)
#제곱수 이용해서 하는 풀이-> 제곱수만 약수의 개수가 홀수개라서 +1해주면 됨