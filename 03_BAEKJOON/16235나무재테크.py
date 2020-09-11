import sys
sys.stdin = open("input.txt", "r")

import collections

N, M, K = map(int, input().split())
trees = [[collections.deque([]) for _ in range(N)] for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)] # 양분
ground = [[5]*N for _ in range(N)]

for _ in range(M):
    x, y, z = tuple(map(int, input().split()))
    trees[x-1][y-1].append(z)

for k in range(K):
    # 봄
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                dead = 0
                for a in range(len(trees[r][c])):
                    if ground[r][c] >= trees[r][c][a]:
                        ground[r][c] -= trees[r][c][a]
                        trees[r][c][a] += 1

                    else:
                        # ground[r][c] += trees[r][c][a] // 2
                        dead += 1

                for _ in range(dead):
                    ground[r][c] += trees[r][c][-1] // 2
                    trees[r][c].pop()



    # 가을
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                for age in trees[r][c]:
                    if age % 5 == 0:
                        for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                            if 0 <= r + dx < N and 0 <= c + dy < N:
                                trees[r+dx][c+dy].appendleft(1)

    # 겨울
    for r in range(N):
        for c in range(N):
            ground[r][c] += A[r][c]
ans = 0
for r in range(N):
    for c in range(N):
        if trees[r][c]:
            ans += len(trees[r][c])
print(ans)









# 봄 / 여름
#     for num in range(len(trees)):
#         x, y, age = trees[num]
#         if ground[x-1][y-1] >= age and not already[x-1][y-1]:
#             ground[x-1][y-1] -= age
#             trees[num][2] += 1  # 나이 + 1
#             survivals.append(trees[num])
#             # survival += 1
#             if trees[num][2] % 5 == 0:
#                 for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
#                     if 0 <= x - 1 + dx < N and 0 <= y - 1 + dy < N:
#                         survivals.append([x + dx, y + dy, 1])
#         else:
#             if not already[x-1][y-1]:
#                 already[x-1][y-1] = 1
#             # 여름 / 만약에 틀리면 이부분 따로 die list 에 넣어서 처리하기
#             ground[x-1][y-1] += age // 2
#
#
#
#             # 여름 / 만약에 틀리면 이부분 따로 die list 에 넣어서 처리하기
#     # 여름
#
#     if len(survivals) == 0:
#         print(0)
#         break
#     trees = survivals
#
#
#
#
# # 가을
# #     for num in range(len(trees)):
# #         x, y, age = trees[num]
# #         if age % 5 == 0:
# #             for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
# #                 if 0 <= x-1+dx < N and 0 <= y-1+dy < N:
# #                     trees.append([x+dx, y+dy, 1])
#
#     if k == K-1:
#         print(len(trees))
#         break
#
# # 겨율
#     for r in range(N):
#         for c in range(N):
#             ground[r][c] += A[r][c]
# print(len(trees))





