arr=[]
for _ in range(10):
    n= int(input())
    if n%42 not in arr:
        arr.append(n%42)
print(len(arr))#배열 길이는 len 쓸 것(count는 뭐와 같은건지 적어야됨)
#set쓰면 중복 제거 가능 