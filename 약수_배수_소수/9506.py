while True:
    arr=[]
    p=0
    a=int(input())
    if a==-1:
        break
    for i in range(a-1):
        if a%(i+1)==0:
            p+=(i+1)
            arr.append(i+1)
    #print(arr)
    if p==a:
        print(a,"=",end=" ")
        print(*arr,sep=" + ")
    else:
        print(a,"is NOT perfect.")
