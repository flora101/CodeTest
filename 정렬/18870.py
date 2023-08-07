# import sys
# input=sys.stdin.readline
# n=int(input())
# arr1=[]
# nums=list(map(int,input().rstrip().split()))
# for i in range(n):
#     arr=[]
#     for j in range(n):
#         if nums[i]>nums[j] and nums[i]!=nums[j]:
#             arr.append(nums[j])
#     arr=list(set(arr))
#     arr1.append(len(arr))
# print(*arr1)
# #시간초과...

n=int(input())
nums=list(map(int,input().rstrip().split()))
nums1=list(set(nums))
nums1.sort()
num={}
for i in range(len(nums1)):
    num[nums1[i]]=i
for i in nums:
    print(num[i],end=' ')