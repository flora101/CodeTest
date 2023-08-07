x=int(input())
i=1
while True:
    x-=i
    if x>0:
        i+=1
    else:
        q=x+i
        break
if i %2==0:
    print(q,"/",i-q+1,sep="")
else:
    print(i-q+1,"/",q,sep="")
