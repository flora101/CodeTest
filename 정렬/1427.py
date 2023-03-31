N=int(input())
s=[]
s=list(map(int,str(N)))
s.sort(reverse=True)
for i in s:
    print(i,end='')