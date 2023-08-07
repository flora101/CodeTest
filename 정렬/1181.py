n=int(input())
arr=[]
for i in range(n):
    s=input()
    arr.append(s)
arr= list(set(arr)) #list로 다시 바꿔줘야지 sort 쓰기 가능
arr.sort()
arr.sort(key=len)
print(*arr,sep="\n")
#
