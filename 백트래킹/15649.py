n,m= map(int,input().split())

def DFS():
    if len(s) == m:
        print(*s)
        return

    for i in range(1, n+1):
        if visited[i]:  # 이미 방문했으면 건너뜀(True)
            continue

        # 방문 안했으면 방문체크 후, 출력 리스트에 넣음(False)
        visited[i] = True
        s.append(i)
        DFS()  # 함수 다시 호출
        s.pop()  # 원상복귀 과정 필요
        visited[i] = False


s = []  # 출력 수열 넣을 리스트 (stack)
visited = [False] * (n+1)  # 방문체크 할 리스트
DFS()
#
