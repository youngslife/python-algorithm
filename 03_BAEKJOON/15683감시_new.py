import sys
sys.stdin = open('input.txt', 'r')


def isntwall(y, x):
    return 0 <= y < N and 0 <= x < M and office[y][x] != 6


def sol(k, k_cnt):
    global cnt
    if k == len(cctvs):
        cnt = min(cnt, k_cnt)

    else:
        y, x, cctv = cctvs[k]
        dir = dirs[cctv]

        for d in dir:
            temp = []
            for dy, dx in d:
                ny, nx = y, x
                while True:
                    ny, nx = ny + dy, nx + dx
                    if isntwall(ny, nx):
                        if office[ny][nx] == 0:
                            temp.append((ny, nx))
                            office[ny][nx] = 7
                    else:
                        break

            sol(k+1, k_cnt-len(temp))

            for ty, tx in temp:
                office[ty][tx] = 0


dirs = [
    [],
    [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],  # 1번
    [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],# 2번
    [[(-1, 0), (0, -1)], [(0, -1), (1, 0)], [(1, 0), (0, 1)], [(0, 1), (-1, 0)]],  # 3번
    [[(0, -1), (1, 0), (0, 1)], [(1, 0), (0, 1), (-1, 0)], [(0, 1), (-1, 0), (0, -1)], [(-1, 0), (0, -1), (1, 0)]],  # 4번
    [[(-1, 0), (1, 0), (0, -1), (0, 1)]]  # 5번
    ]

N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
cctvs = []

for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctvs.append((i, j, office[i][j]))
        elif office[i][j] == 0:
            cnt += 1

sol(0, cnt)
print(cnt)



