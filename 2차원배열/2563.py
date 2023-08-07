board=[[0 for _ in range(101)] for _ in range(101)]
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    for i in range(a,a+10):
        for j in range(b,b+10):
            board[i][j]=1
cnt=0
for i in board:
    cnt+=i.count(1)
print(cnt)
#
