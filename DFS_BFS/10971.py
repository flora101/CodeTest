import sys
N = int(input())
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize

def dfs(start, next, value, visited):
    global min_value

    if len(visited) == N:
        if travel_cost[next][start] != 0:
            min_value = min(min_value, value + travel_cost[next][start])
            return
 
    for i in range(N):
        if travel_cost[next][i] != 0 and i not in visited and value < min_value: 
            visited.append(i)
            dfs(start, i, value + travel_cost[next][i], visited)
            visited.pop()


for i in range(N):
    dfs(i, i, 0, [i])
print(min_value)
 


'''
N= int(input())
maps=[]
for _ in range(N):
    maps.append(list(map(int,input().split())))
visited= [0]*N
tmp=1000000
add=0

def dfs(i,add,visited):
    global tmp
    if add> tmp:
        return
    if sum(visited)==N-1:
        if maps[i][0]:
            tmp=min(tmp,add+maps[i][0])
            return
    for j in range(1,N):
        if maps[i][j] and visited[j]==0:
            visited[j]=1
            dfs(j,add+maps[i][j],visited)
            visited[j]=0
            
            
for i in range(1,N):
    if maps[0][i]:
        visited[i]=1
        dfs(i,add+maps[0][i],visited)
        visited[i]=0 #why???
print(tmp)
'''