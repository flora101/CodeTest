max,x,y=0,0,0
for i in range(9):
    arr= list(map(int, input().split()))
    for j in range(9):
        if arr[j]>max:
            max,x,y=arr[j],i,j
print(max)
print(x+1,y+1)
#