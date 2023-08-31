def solution(n):
    if n == 0:
        return "-"
    return solution(n - 1) + " " * (3 ** (n - 1)) + solution(n - 1)
while 1:
    try:
        N = int(input())
        print(solution(N))
    except EOFError:
        break
#
