N,K = map(int,input().split())
graph= []
for _ in range(N):
    graph.append(int(input()))
graph.sort(reverse=True)
cnt= 0
for i in range(N):
    if K // int(graph[i]) >=1:
        cnt += K //int(graph[i])
        K %= int(graph[i])
print(cnt)