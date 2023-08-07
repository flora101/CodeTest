score_list=['A+','A0','B+','B0','C+','C0','D+','D0']
score=0
sum_b=0
for i in range(20):
    a,b,c=input().split()
    if c in score_list:
        #print(4.5-score_list.index(c)*0.5)
        c=4.5-score_list.index(c)*0.5
    elif c == 'F':
        c=0
    elif c=='P':#p,f차이를 안둬서 좀 틀렸었음
        b=0
        c=0
    score += float(b)*c
    sum_b+=float(b)
print(score/sum_b)