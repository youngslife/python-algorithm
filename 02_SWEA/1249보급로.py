import sys
sys.stdin = open('input.txt', 'r')

# 복구시간 == 깊이비례
# 복구시간이 가장 짧은 경로에 대한 복구 시간
# bfs로 완전탐색하고 이전 값 보다 커질 시 break해보자.

def bfs(i, j):
    q = [(i, j)]
    visited[i][j] = 1

    while q:
        y, x = q.pop(0)
        for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
            yy = y + dy
            xx = x + dx
            if yy == N-1 and xx == N-1 and not q:
                if not visited[yy][xx]:
                    q.append((yy, xx))
                    visited[yy][xx] = visited[y][x] + arr[yy][xx]
                elif visited[yy][xx] > visited[y][x] + arr[yy][xx]:
                    q.append((yy, xx))
                    visited[yy][xx] = visited[y][x] + arr[yy][xx]
                return
            elif 0 <= yy < N and 0 <= xx < N:
                if not visited[yy][xx]:
                    q.append((yy, xx))
                    visited[yy][xx] = visited[y][x] + arr[yy][xx]
                elif visited[yy][xx] > visited[y][x] + arr[yy][xx]:
                    q.append((yy, xx))
                    visited[yy][xx] = visited[y][x] + arr[yy][xx]



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    bfs(0, 0)
    print('#%d %d' % (tc, visited[N-1][N-1]-1))

