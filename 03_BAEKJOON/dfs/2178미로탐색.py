import sys
sys.stdin = open('input.txt', 'r')


def bfs(i, j):
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    q = [(i, j)]
    visited = [[0]*M for _ in range(N)]
    visited[i][j] = 1
    while q:
        y, x = q.pop(0)

        for n in range(4):
            Y = y + dy[n]
            X = x + dx[n]
            if 0 <= Y < N and 0 <= X < M and not visited[Y][X]:
                if Y == N - 1 and X == M - 1:
                    return visited[y][x] + 1
                elif arr[Y][X] == '1':
                    q.append((Y, X))
                    visited[Y][X] = visited[y][x] + 1


N, M = map(int, input().split())
arr = [input() for _ in range(N)]
print(arr)
print(bfs(0, 0))

# 115660KB / 156 ms
