arr=[i+1 for i in range(30)]
#print(arr)
for _ in range(28):
    n= int(input())
    arr.remove(n)
print(*arr,sep="\n")#한줄 띄우기 하려면 sep 쓰기
#