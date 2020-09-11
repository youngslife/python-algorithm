import sys
sys.stdin = open("input.txt", "r")

R, C, M = map(int, input().split())  # M은 상어의 수
arr = [[0]*C for _ in range(R)]
sharks = [0]*(M+1)  # 상어 위치
        #위 아래 오 왼
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]

for n in range(1, 1+M):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1] = n  # 상어 번호(1 ~ M)
    sharks[n] = [s, d, z]  # 속력, 방향, 크기
print('1', arr)

king = -1  # 낚시왕의 위치(-1(시작점)<= king <= C(도착위치))
ans = 0

for _ in range(C):
    print(sharks)
    print('change', arr)
    king += 1  # situation 1
    for j in range(R):
        if arr[j][king]:
            ans += sharks[arr[j][king]][2]  # situation 2-1
            arr[j][king] = 0  # situation 2-2
            sharks[arr[j][king]] = 0  # 상어리스트에서 없애기
            break
    print('2', arr)

    # situation 3 (상어 이동)
    temp = [[0]*C for _ in range(R)]  # 임시 상어 위치
    for i in range(R):
        for j in range(C):
            if arr[i][j]:
                y = i
                x = j
                n = arr[y][x]  # 상어 번호

                # cnt = 0
                # print(sharks[n][1], 'check')
                print((y, x))

                if sharks[n][1] == 1 or sharks[n][1] == 2:
                    if sharks[n][0] >= ((R - 1) * 2):
                        print('a')
                        remain = sharks[n][0] % ((R-1)*2)
                    else:
                        print('b')
                        remain = sharks[n][0]
                else:
                    if sharks[n][0] >= ((C - 1) * 2):
                        print('c', sharks[n][0])
                        remain = sharks[n][0] % ((C - 1) * 2)
                    else:
                        print('d')
                        remain = sharks[n][0]
                print('start', y, x, remain, sharks[n][1])

                for idx in range(remain):
                    print(idx, y, x)

                    if idx == 0 and:
                        y += dy[sharks[n][1]]
                        x += dx[sharks[n][1]]

                    if sharks[n][1] == 1 or sharks[n][1] == 2:

                        if y == 0 or y == R - 1:
                            if sharks[n][1] == 1:
                                sharks[n][1] = 2
                            elif sharks[n][1] == 2:
                                sharks[n][1] = 1
                    elif sharks[n][1] == 3 or sharks[n][1] == 4:
                        if x == 0 or x == C - 1:
                            if sharks[n][1] == 3:
                                sharks[n][1] = 4
                            elif sharks[n][1] == 4:
                                sharks[n][1] = 3

                    if idx == 0:
                        continue
                    y += dy[sharks[n][1]]
                    x += dx[sharks[n][1]]

                    print(y, x)
                print('final', y, x)
                if not temp[y][x]:
                    temp[y][x] = n
                else:
                    if sharks[n][2] > sharks[temp[y][x]][2]:
                        temp[y][x] = n
                print('temp', temp)

    #             for _ in range(sharks[n][0]):
    #                 if y == 0 or y == R - 1 or x == 0 or x == C - 1:
    #                     break
    #                 cnt += 1
    #                 y += dy[sharks[n][1]]
    #                 x += dx[sharks[n][1]]
    #
    #             print(y, x, 'now')
    #             if sharks[n][1] == 1:
    #                 sharks[n][1] = 2
    #             elif sharks[n][1] == 2:
    #                 # print(sharks[n], sharks[n][1])
    #                 sharks[n][1] = 1
    #             elif sharks[n][1] == 3:
    #                 sharks[n][1] = 4
    #             elif sharks[n][1] == 4:
    #                 sharks[n][1] = 3
    #             print(sharks[n][1], 'check2')
    #
    #             if sharks[n][1] == 1 or sharks[n][1] == 2:
    #                 remain = sharks[n][0] - cnt
    #                 after = remain % ((R-1)*2)
    #                 for _ in range(after):
    #                     y += dy[sharks[n][1]]
    #                     x += dx[sharks[n][1]]
    #             else:
    #                 remain = sharks[n][0] - cnt
    #                 after = remain % ((C-1)*2)
    #                 print(after)
    #                 for _ in range(after):
    #                     y += dy[sharks[n][1]]
    #                     x += dx[sharks[n][1]]
    #
    #             print(y, x)
    #             # temp[y][x] = n
    #             if not temp[y][x]:
    #                 temp[y][x] = n
    #             else:
    #                 if sharks[n][2] > sharks[temp[y][x]][2]:
    #                     temp[y][x] = n
    # print('temp', temp)
    arr = temp
print(ans)

                # if sharks[n][1] == 2:
                #     cnt = 0
                #     while y == 0 or y == R-1 or x == 0 or x == C-1:
                #         cnt += 1
                #         y += dy[2]
                #         x += dx[2]
                # 방향 전환
                #     sharks[n][1] == 1
                #     remain = sharks[n][0]-cnt
                #     after = remain % R
                #     for _ in range(after):
                #         y += dy[1]
                #         x += dx[1]
                # temp[y][x] = n
    #             print(temp)
    #             break
    #     break
    # break

