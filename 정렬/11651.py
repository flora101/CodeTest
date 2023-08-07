n=int(input())
arr=[]
for i in range(n):
    x,y=map(int,input().split())
    arr.append([x,y])
arr.sort(key=lambda x:(x[1],x[0]))#첫번째 인자를 기준으로 먼저 오름차순 정렬, 두번째 인자를 기준으로 다시 오름차순 정렬
for i in arr:
    print(i[0],i[1])