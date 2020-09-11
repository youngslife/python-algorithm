import sys
sys.stdin = open('input3.txt', 'r')

def bfs(i, j, cnt):
    global res
    visited = [[0]*N for _ in range(N)]
    temp = 0

    q = [(i, j)]
    if arr[i][j] == 1:
        temp += 1

    visited[i][j] = 1
    for _ in range(cnt):
        for _ in range(len(q)):
            y, x = q.pop(0)
            for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                Y = y + dy
                X = x + dx
                if 0 <= Y < N and 0 <= X < N and not visited[Y][X]:
                    q.append((Y, X))
                    visited[Y][X] = 1
                    if arr[Y][X] == 1:
                        temp += 1
    # print('tempt', temp)
    return temp


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0

    for k in range(N+2, 0, -1):
        expense = k*k + (k-1)*(k-1)
        candi = 0
        for i in range(N):
            for j in range(N):
                home = bfs(i, j, k-1)
                if home * M - expense >= 0:
                    if home > candi:
                        candi = home
        if res < candi:
            res = candi

    print('#%d %d' %(tc, res))



