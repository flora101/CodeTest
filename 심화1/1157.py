arr=[]
word = input()
word= word.upper()
word_list=list(set(word))
for i in word_list:
    cnt=word.count(i)
    arr.append(cnt)
if arr.count(max(arr))>=2:
    print("?")
else:
    print(word_list[arr.index(max(arr))])
##
