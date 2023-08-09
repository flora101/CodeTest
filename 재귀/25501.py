def recursion(s, l, r):
    global cnt #함수 안에서 전역으로 쓰고싶으면 global 선언하기
    cnt+=1

    if l >= r: 
        return 1
    elif s[l] != s[r]: 
        return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t=int(input())

for i in range(t):
    cnt=0
    word=input()
    print(isPalindrome(word),cnt)
