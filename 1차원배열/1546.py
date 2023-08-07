n=int(input())
test = list(map(int,input().split()))#일렬로 받을땐 이렇게 
test_max= max(test)
score=0
for i in range(n):
    test[i]=test[i]/test_max*100
    score+=test[i]
print(score/n)
