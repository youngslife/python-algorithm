import sys
sys.stdin = open('input.txt', 'r')

import collections


def bfs(q):
    cnt = -1
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    while q:
        for _ in range(len(q)):
            y, x = q.popleft()
            for n in range(4):
                Y = y + dy[n]
                X = x + dx[n]
                if 0 <= Y < N and 0 <= X < M:
                    if box[Y][X] == 0:
                        box[Y][X] = 1
                        q.append((Y, X))
        cnt += 1
    return cnt

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
# print(box)

q = collections.deque([])

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))

result = bfs(q)

flag = False
for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            result = -1
            flag = True
            break
    if flag:
        break
print(result)

# 161004 KB / 566 ms
# bfs경우 함수 호출하지 않고 밑에서 바로 수행해도 됨.
# 미리 tomato cnt 하고 -1 씩해주고 tomato cnt 가 남으면 -1출력, 그렇지 않으면 time cnt 출력하면 시간 아낄 수 있음.
