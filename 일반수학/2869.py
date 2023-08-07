import sys
input=sys.stdin.readline
# a,b,v=map(int,input().split())
# i=0
# p=0
# while True:
#     i+=1
#     p=(a-b)*i
#     if p+a>=v:
#         print(i+1)
#         break
#시간 초과 뜸

a,b,v=map(int,input().split())
day=(v-b)/(a-b)
print(int(day) if day==int(day) else int(day)+1)