num_list= ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word=list(input())
res=0
for i in word:
    for j in num_list:
        if i in j:
            res+=num_list.index(j)+3

print(res)
#