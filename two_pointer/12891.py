import sys
input = sys.stdin.readline

s,p = map(int,input().split())
dna = input()
a,c,g,t = map(int,input().split())
left = 0
right = p-1
dna1 = dna[:right+1]

rna = []
rna.append(dna1.count("A"))
rna.append(dna1.count("C"))
rna.append(dna1.count("G"))
rna.append(dna1.count("T"))

answer = 0
# print(rna)
while right < s:
    if rna[0]>=a and rna[1]>=c and rna[2]>=g and rna[3]>=t:
        answer+=1
    if dna[left]=="A":
        rna[0]-=1
    elif dna[left]=="C":
        rna[1]-=1
    elif dna[left]=="G":
        rna[2]-=1
    else:
        rna[3]-=1
    left+=1
    right+=1
    if dna[right]=="A":
        rna[0]+=1
    elif dna[right]=="C":
        rna[1]+=1
    elif dna[right]=="G":
        rna[2]+=1
    else:
        rna[3]+=1
    # print(rna)
print(answer)
