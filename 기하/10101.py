arr=[]
for _ in range(3):
    a=int(input())
    arr.append(a)
if sum(arr)!=180:
    print("Error")
elif arr[0]==arr[1]==arr[2]==60:
    print("Equilateral")
elif sum(arr)==180 and (arr[0]!=arr[1] and arr[0]!=arr[2] and arr[1]!=arr[2]):
    print("Scalene")
elif sum(arr)==180 and (arr[0]==arr[1] or arr[0]==arr[2] or arr[1]==arr[2]):
    print("Isosceles")
    