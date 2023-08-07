import sys
input= sys.stdin.readline
N=int(input())
arr = list(map(int,input().split()))
v=int(input())
print(arr.count(v))

#.count(s):s와 같은게 몇개 있는지 세어줌