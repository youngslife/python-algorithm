import sys
sys.stdin = open("input4861.txt", "r")
# M 길이 만큼의 문자열 동안 앞뒤가 같은걸 찾아야해
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        # arr += input().split()
        arr.append(list(input()))  # 이차원 배열

<<<<<<< HEAD
        # letter_board = [input() for i in range(N)]

    # print(arr)
    print(M)
=======

    print(arr)
>>>>>>> dca2aa51df90cb0eec94608b2dacd01ec097412a
    for i in range(len(arr)):
        for j in range(N):
            origin = arr[i][j:j+M]  # 전체 텍스트
        # origin = arr[i]
            rev = origin[::-1]  # 찾을 패턴

            # print(origin, rev)
            # Brute Force방법을 리스트에서 사용
            p = 0  # rev의 인덱스
            t = 0  # origin 인덱스
            if len(origin) == M:
                while p < len(rev) and t < len(origin):
                    if origin[t] != rev[p]:
                        t = t - p
                        p = -1
                    t = t + 1
                    p = p + 1
                if p == len(rev):
                    print('#{}'.format(tc), end=" ")
                    for m in origin:
                        print(m, end="")
                    print()

    # 전치행렬:  letter_board_rotation = list(zip(*letter_board))


    c = []
    col = []
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            c.append(arr[i][j])
        col.append(c)
        c = []

    for k in range(len(col)):
        for j in range(N):
            ori = col[k][j:j + M]
            re = ori[::-1]

            p = 0
            t = 0

            if len(ori) == M:
                while p < len(re) and t < len(ori):
                    if ori[t] != re[p]:
                        t = t - p
                        p = -1
                    t = t + 1
                    p = p + 1
                if p == len(re):
                    print('#{}'.format(tc), end=" ")
                    for m in ori:
                        print(m, end="")
                    print()

# 세로는 i, j만 바꿔주면됨
# def find():
#     for i in range(N-M+1):
#         k = 0
#         h = M//2
#         while k <h:
#             if s[i][j+k] != s[i][j+M-k-1]:
#                 break
#             k +=1
#         if k == h:
#             print(s[i][j:j+M])
#             return
#
#         k = 0
#         while k<h:
#             if s[j+k][i] != s[j+M-k-1]:
#                 break
#             k +=1
#         if k ==h:
#             for l in range(j, j+M):
#                 print(s[l][i], end="")



    # P = len(str1)
    # T = len(str2)
    #
    # i = 0
    # j = 0
    # while j < P and i < T:
    #     if str2[i] != str1[j]:
    #         i = i - j
    #         j = -1
    #     i = i + 1
    #     j = j + 1
    # if j == P:
    #     print('#{} 1'.format(tc))
    # else:
    #     print('#{} 0'.format(tc))

    # for i in range(len(arr)):
    #     l = len(arr[i]) // 2
    #     print(l)
    #     for j in range(l):
    #         if arr[i][j] == arr[i][-j]:
    #             print(arr[i])
    #             break