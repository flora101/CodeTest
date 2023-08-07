#틀린 내 풀이...
# n=int(input())
# num=list(map(int,input().split()))
# stack=[]
# stack2=[]
# idx=1
# p=0
# for i in num:
#     if i != idx:
#         stack2.append(i)
#     elif i==idx:
#         stack.append(i)
#         idx+=1
# if (len(stack)+len(stack2))==n:
#     while len(stack2)!=0:
#         a = stack2.pop()
#         if a==idx:
#             idx+=1
#         else:
#             p=1
#             break
# if p==0:
#     print("Nice")
# else:
#     print("Sad")

#정답 풀이
n = int(input())
standing = list(map(int, input().split()))
stack = []
idx = 1
 
while standing:
    if standing[0] == idx:
        standing.pop(0)
        #print(standing.pop(0))
        idx += 1
    else:
        stack.append(standing.pop(0))
 
    while stack:
        if stack[-1] == idx:
            stack.pop()
            idx += 1
        else:
            break
 
if not stack: 
    print('Nice')
else:
    print('Sad')

#pop(0)을 쓰면 스택에 젤 밑에 있는 게 없어진다는 점을 알게되었다.