import sys
sys.stdin = open("5188.txt", "r")

dy = [0, 1]  # 우 하
dx = [1, 0]


def dfs(y, x, s):
    global res
    if s > res:
        return

    if y == N-1 and x == N-1:
        res = s
        return

    for n in range(2):
        Y = y + dy[n]
        X = x + dx[n]
        if 0 <= Y < N and 0 <= X < N:
            dfs(Y, X, s + arr[Y][X])


for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 10 ** 13

    dfs(0, 0, arr[0][0])
    print('#%d %d' % (tc, res))



