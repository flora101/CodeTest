A, P= map(int,input().split())
num=[A] #[57]

while True:
    sum=0
    for i in str(num[-1]):
        sum += int(i)**P #i를 꼭 int로 바꿔주기
    if sum in num:
        break
    num.append(sum)
print(num.index(sum))