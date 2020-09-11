import sys
sys.stdin = open("4875.txt", "r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def isnotWall(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True


def isStreet(x, y):
    return mat[x][y] == 0 or mat[x][y] == 3


def dfs(x, y):
    global result

    if mat[x][y] == 3:
        result = 1
        return

    visited.append((x, y))
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if isnotWall(X, Y)and isStreet(X, Y) and ((X, Y) not in visited):
            dfs(X, Y)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]

    visited = []
    result = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 2:
                x = i
                y = j

    dfs(x, y)

    print('#%d %d'%(tc, result))



