n,m=map(int,input().split())
arr=[i+1 for i in range(n)]
#print(arr)
for _ in range(m):
    i,j=map(int,input().split())
    temp= arr[i-1]
    arr[i-1]=arr[j-1]
    arr[j-1]=temp
    #print(arr)
for i in range(n):
    print(arr[i],end= " ")
#print(*arr) #배열의 수만 떼고 싶으면 이렇게 하기