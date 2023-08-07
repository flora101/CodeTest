word=input()
long= len(word)
tf=1
#print(len(word)//2)
for i in range(long//2):
    if word[i]!=word[long-i-1]:
        tf=0
        break
    else:
        continue
print(tf)