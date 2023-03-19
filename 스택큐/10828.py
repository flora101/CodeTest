import sys
input=sys.stdin.readline
N=int(input())
stack=[]

for _ in range(N):
    x=input().split()
    if x[0]== "push":
        stack.append(x[1])
    elif x[0]=="pop":
        if not stack:
            print("-1")
        else:
            print(stack.pop())
    elif x[0]=="top":
        if not stack:
            print("-1")
        else:
            print(stack[-1])
    elif x[0]=="size":
        print(len(stack))
    elif x[0] =="empty":
        if not stack:
            print("1")
        else:
            print("0")