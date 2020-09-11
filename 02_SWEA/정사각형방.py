import sys
sys.stdin = open('3.txt', 'r')
# 상하좌우 방 이동(방 존재, 이동하려는 방의 숫자가 현재방 보다 +1일때)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def dfs(y, x):
    global cnt
    stack = [(y, x)]
    # visited[y][x] = 1
    while stack:
        # cur_visited = [[0] * N for _ in range(N)]
        y, x = stack.pop(-1)
        cnt += 1
        for n in range(4):
            Y = y + dy[n]
            X = x + dx[n]
            if 0 <= Y < N and 0 <= X < N:
                if room[y][x]+1 == room[Y][X]:
                    # if not visited[Y][X]:
                    stack.append((Y, X))
                    visited[Y][X] = 1
                        # cur_visited[Y][X] = 1
                        # dfs(Y, X, room[Y][X])



for tc in range(1, 1+int(input())):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    maxi = 1
    nums = N*N
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
            # cur_visited = [[0]*N for _ in range(N)]
                cnt = 0
                dfs(i, j)
                if cnt > maxi:
                    maxi = cnt
                    nums = room[i][j]
                elif cnt == maxi:
                    if nums > room[i][j]:
                        nums = room[i][j]

    print('#%d %d %d' % (tc, nums, maxi))


# Recursion exceed
# def dfs(y, x):
#     global cnt
#     # visited[y][x] = 1
#     for n in range(4):
#         Y = y + dy[n]
#         X = x + dx[n]
#         if 0 <= Y < N and 0 <= X < N:
#             if room[y][x]+1 == room[Y][X]:
#                 # if not visited[Y][X]:  +1로만 가니까 visit체크 안해도 될듯?
#                 visited[Y][X] = 1
#                 cnt += 1
#                 dfs(Y, X)
#                 break
#
#
# for tc in range(1, 1+int(input())):
#     N = int(input())
#     room = [list(map(int, input().split())) for _ in range(N)]
#     maxi = 1
#     nums = N*N
#     visited = [[0] * N for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             if not visited[i][j]:
#                 # visited = [[0]*N for _ in range(N)]
#                 cnt = 1
#                 visited[i][j] = 1
#                 dfs(i, j)
#                 if cnt > maxi:
#                     maxi = cnt
#                     nums = room[i][j]
#                 elif cnt == maxi:
#                     if nums > room[i][j]:
#                         nums = room[i][j]
#
#     print('#%d %d %d' % (tc, nums, maxi))


