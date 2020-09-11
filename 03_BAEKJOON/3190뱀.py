import sys
sys.stdin = open("input.txt", "r")
# 115688 KB / 144 ms
N = int(input())
K = int(input())  # 사과의 개수
board = [[0]*N for _ in range(N)]

now = 3  # 현재방향
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

x, y = 0, 0  # 뱀 현재 위치

turn = [0]*10001
q = [(0, 0)]

for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 'a'  # 'a'== 사과

L = int(input())
for _ in range(L):
    t, d = input().split()
    turn[int(t)] = d

time = 0
for t in turn:
    time += 1
    if t:
        if t == 'L':  # 왼쪽
            now = (now - 1) % 4
        elif t == 'D':  # 오른쪽
            now = (now + 1) % 4

    xx = x + dx[now]
    yy = y + dy[now]

    if 0 <= xx < N and 0 <= yy < N:
        if (yy, xx) in q:
            break
        else:
            q.append((yy, xx))
            x = xx
            y = yy
            if board[yy][xx]:
                board[yy][xx] = 0
            else:
                q.pop(0)
    else:
        break
print(time)

# N = int(input())
# K = int(input())  # 사과의 개수
# board = [[0]*N for _ in range(N)]
#
# now = 3  # 현재방향
# dy = [1, 0, -1, 0]
# dx = [0, -1, 0, 1]
#     # 0, 1, 2, 3
#
# # x, y = 0, 0  # 뱀 현재 위치
#
#
# turn = [0]*10001
# q = [(0, 0)]
#
# for _ in range(K):
#     i, j = map(int, input().split())
#     board[i-1][j-1] = 'a'  # 'a'== 사과
#
# L = int(input())
# for _ in range(L):
#     t, d = input().split()
#     turn[int(t)] = d
#
# time = 0
#
# for t in turn:
#     time += 1
#
#     if t:
#         if t == 'L':  # 왼쪽
#             now = abs((now - 1)) % 4
#         elif t == 'D':  # 오른쪽
#             now = (now + 1) % 4
#
#     yy = q[-1][0] + dy[now]
#     xx = q[-1][1] + dx[now]
#
#
#     if 0 <= xx < N and 0 <= yy < N:
#         if (yy, xx) in q:
#             break
#         else:
#             q.append((yy, xx))
#
#             if board[yy][xx]:
#                 board[yy][xx] = 0
#             else:
#                 q.pop(0)
#     else:
#         break
# print(time)
#
#
#
