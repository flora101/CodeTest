N=int(input())
n= N//5
for i in range(n,-1,-1):
    if (N-i*5)% 3 ==0:
        print (i+(N-i*5)//3)
        break
else:
    print(-1)