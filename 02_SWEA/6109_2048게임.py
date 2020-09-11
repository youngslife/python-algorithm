import sys
sys.stdin = open("6109.txt", "r")

def up(arr, N):
    # 공백(0)을 다 없애줌
    for i in range(N - 1):
        for j in range(N):
            if arr[i][j] == 0:
                for n in range(i, N):
                    if arr[n][j]:
                        arr[i][j], arr[n][j] = arr[n][j], 0
                        break

    # i번째줄의 j와 i+1번째 줄의 j 가 같으면
    for i in range(N - 1):
        for j in range(N):
            if arr[i][j] == arr[i + 1][j]:
                arr[i][j] *= 2
                arr[i + 1][j] = 0

    for i in range(N - 1):
        for j in range(N):
            if arr[i][j] == 0:
                for n in range(i, N):
                    if arr[n][j]:
                        arr[i][j], arr[n][j] = arr[n][j], 0
                        break
    return arr


def down(arr, N):
    for i in range(N-1, 0, -1):
        for j in range(N):
            if arr[i][j] == 0:
                for n in range(i-1, -1, -1):
                    if arr[n][j]:
                        arr[i][j], arr[n][j] = arr[n][j], 0
                        break

    for i in range(N-1, 0, -1):
        for j in range(N):
            if arr[i][j] == arr[i-1][j]:
                arr[i][j] *= 2
                arr[i-1][j] = 0

    for i in range(N-1, 0, -1):
        for j in range(N):
            if arr[i][j] == 0:
                for n in range(i-1, -1, -1):
                    if arr[n][j]:
                        arr[i][j], arr[n][j] = arr[n][j], 0
                        break
    return arr

def right(arr, N):
    for i in range(N):
        for j in range(N-1, -1, -1):
            if arr[i][j] == 0:
                for n in range(j-1, -1, -1):
                    if arr[i][n]:
                        arr[i][j], arr[i][n] = arr[i][n], 0
                        break

    for i in range(N):
        for j in range(N-1, 0, -1):
            if arr[i][j] == arr[i][j-1]:
                arr[i][j] *= 2
                arr[i][j-1] = 0

    for i in range(N):
        for j in range(N-1, -1, -1):
            if arr[i][j] == 0:
                for n in range(j-1, -1, -1):
                    if arr[i][n]:
                        arr[i][j], arr[i][n] = arr[i][n], 0
                        break
    return arr


def left(arr, N):
    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == 0:
                for n in range(j, N):
                    if arr[i][n]:
                        arr[i][j], arr[i][n] = arr[i][n], 0
                        break

    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                arr[i][j] *= 2
                arr[i][j+1] = 0

    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == 0:
                for n in range(j, N):
                    if arr[i][n]:
                        arr[i][j], arr[i][n] = arr[i][n], 0
    return arr

for tc in range(1, 1 + int(input())):
        info = input().split()
        N = int(info[0])
        d = info[1]  # 방향 인덱스

        arr = [list(map(int, input().split())) for _ in range(N)]

        if d == 'up':
            result = up(arr, N)
        elif d == 'down':
            result = down(arr, N)

        elif d == 'left':
            result = left(arr, N)

        elif d == 'right':
            result = right(arr, N)

        print('#%d'%tc)
        for i in range(N):
            for j in range(N):
                print(result[i][j], end=" ")
            print()

        # 공백(0)을 다 없애줌
        # for y in range(N - 1):
        #     for x in range(N):
        #         if arr[y][x] == 0:
        #             arr[y][x], arr[y + dy[d]][x + dx[d]] = arr[i + 1][j], 0
        # print(arr)
        # # i번째줄의 j와 i+1번째 줄의 j 가 같으면
        # for i in range(N - 1):
        #     for j in range(N):
        #         if arr[i][j] == arr[i + 1][j]:
        #             arr[i][j] *= 2
        #             arr[i + 1][j] = 0
        # print(arr)
        #
        # for i in range(N - 1):
        #     for j in range(N):
        #         if arr[i][j] == 0:
        #             for n in range(i, N):
        #                 if arr[n][j]:
        #                     arr[i][j], arr[n][j] = arr[n][j], 0
        #                     break
        # print(arr)


# directions = ['up', 'down', 'left', 'right']
# rng = [[0, 1], [1, 0], [0, 1], [1, 0]]
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
#
#
#
# print(directions.index('down'))
#
# for tc in range(1, 1+int(input())):
#     info = input().split()
#     N = int(info[0])
#     d = directions.index(info[1])  # 방향 인덱스
#     print('dir', d)
#     print(info, N, d)
#
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     print(arr)
# # 공백(0)을 다 없애줌
#     for y in range(rng[d][0], N-rng[d][1]):
#         for x in range(N):
#             if arr[y][x] == 0:
#                 arr[y][x], arr[y+dy[d]][x+dx[d]] = arr[y+dy[d]][x+dx[d]], 0
#     print(arr)
# # i번째줄의 j와 i+1번째 줄의 j 가 같으면
#     for y in range(rng[d][0], N-rng[d][1]):
#         for x in range(N):
#             if arr[y][x] == arr[y+dy[d]][x+dx[d]]:
#                 arr[y][x] *= 2
#                 arr[y+dy[d]][x+dx[d]] = 0
#     print(arr)
#
#     for y in range(rng[d][0], N-rng[d][1]):
#         for x in range(N):
#             if arr[y][x] == 0:
#                 for n in range(y, N):
#                     if arr[n][x]:
#                         arr[y][x], arr[n][x] = arr[n][x], 0
#                         break
#     print(arr)

    # for tc in range(1, 1 + int(input())):
    #     info = input().split()
    #     N = int(info[0])
    #     d = directions.index(info[1])  # 방향 인덱스
    #     print('dir', dir)
    #     print(info, N, dir)
    #
    #     arr = [list(map(int, input().split())) for _ in range(N)]
    #
    #     print(arr)
    #     # 공백(0)을 다 없애줌
    #     for y in range(N - 1):
    #         for x in range(N):
    #             if arr[y][x] == 0:
    #                 arr[y][x], arr[y + dy[d]][x + dx[d]] = arr[i + 1][j], 0
    #     print(arr)
    #     # i번째줄의 j와 i+1번째 줄의 j 가 같으면
    #     for i in range(N - 1):
    #         for j in range(N):
    #             if arr[i][j] == arr[i + 1][j]:
    #                 arr[i][j] *= 2
    #                 arr[i + 1][j] = 0
    #     print(arr)
    #
    #     for i in range(N - 1):
    #         for j in range(N):
    #             if arr[i][j] == 0:
    #                 for n in range(i, N):
    #                     if arr[n][j]:
    #                         arr[i][j], arr[n][j] = arr[n][j], 0
    #                         break
    #     print(arr)