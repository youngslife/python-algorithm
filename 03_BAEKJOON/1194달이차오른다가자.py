import sys
sys.stdin = open('input.txt', "r")


def bfs(y, x, k):
    q = [(y, x, k)]

    while q:
        y, x, k = q.pop()
        if arr[y][x] == '1':
            print(visited[y][x][k])
            return

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            X, Y, K = x + dx, y + dy, k
            if X < 0 or X >= M or Y < 0 or Y >= N:
                continue
            c = arr[Y][X]
            print(K)

            if c.islower():
                K |= (1 << (ord(c)-ord('a'))) # 합집합
            elif c.isupper() and not K & (1 << ord(c)-ord('A')):
                continue
            if not visited[Y][X][K] and c != '#':
                q.append((Y, X, K))
                0
                visited[Y][X][K] = visited[Y][X][K] + 1
    print(-1)



N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
print(visited)

res = -1


for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            bfs(i, j, 0)

