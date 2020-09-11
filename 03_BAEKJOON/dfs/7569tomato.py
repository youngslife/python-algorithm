import sys
sys.stdin = open('input.txt', 'r')

import collections

M, N, H = map(int, input().split())
box = [0]*H
for f in range(H):
    floor = [list(map(int, input().split())) for _ in range(N)]
    box[f] = floor

q = collections.deque([])
unripe = 0

for f in range(H):
    for i in range(N):
        for j in range(M):
            if box[f][i][j] == 1:
                q.append((f, i, j))
            elif box[f][i][j] == 0:
                unripe += 1

if not unripe:
    print(0)
else:
    cnt = 0
    while q:
        for _ in range(len(q)):
            z, y, x = q.popleft()
            for dz, dy, dx in (0, 1, 0), (0, -1, 0), (0, 0, -1), (0, 0, 1), (1, 0, 0), (-1, 0, 0):
                Z, Y, X = z+dz, y+dy, x+dx
                if 0<=Z<H and 0<=Y<N and 0<=X<M and not box[Z][Y][X]:
                    box[Z][Y][X] = 1
                    unripe -= 1
                    # print(Z, Y, X)
                    q.append((Z, Y, X))
            # print('a', unripe)
        cnt += 1
        if not unripe:  # 여기서 안 끊어 주면 while q 를 한 번 도 돌게 되므로 시간이 더 걸림.
            break

    if unripe:
        print(-1)
    else:
        print(cnt)

# 222924 KB / 792ms
