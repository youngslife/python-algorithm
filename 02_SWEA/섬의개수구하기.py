import sys
sys.stdin = open('island.txt', 'r')

dy = [0, 0, -1, 1, -1, 1, 1, -1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]

def dfs(y, x):
    visited[y][x] = 1
    for n in range(8):
        if arr[y+dy[n]][x+dx[n]] and not visited[y+dy[n]][x+dx[n]]:
            arr[y+dy[n]][x+dx[n]] = 0
            # visited[y+dy[n]][x+dx[n]] = 1
            dfs(y + dy[n], x + dx[n])

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [[0]*(N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+2)]
    visited = [[0]*(N+2) for _ in range(N+2)]

    cnt = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)