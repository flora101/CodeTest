#1->2~7->8~19->20~37->38~61까지, 1,6,12,18
n=int(input())
n-=1
i=1
while True:
    p=6*i
    i+=1
    if n>0:
        n-=p
    else:
        print(i-1)
        break
