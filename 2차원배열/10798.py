arr=[list(input().rstrip()) for i in range(5)]
max=0
for i in arr:
    if len(i)>max:
        max=len(i)

for i in range(max):
    for j in range(5):
        try:
            print(arr[j][i],end="")
        except:
            pass
##