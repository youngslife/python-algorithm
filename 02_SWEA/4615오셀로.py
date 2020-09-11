import sys
sys.stdin = open("4615.txt", "r")
# 상 하 좌 우 대각선
dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

def check(mat, x, y, color):
    for i in range(4):
        a = y
        b = x
        # print('a, b', a, b)
        while 0 <= x < N and 0 <= y < N:
            y += dy[i]
            x += dx[i]
            # print('y, x', y, x)
            if x == -1 or y == -1 or x == N or y == N:
                break
            elif mat[y][x] == 0:
                break
            elif mat[y][x] != color:
                # print('matvalue', mat[y][x])
                continue
            elif mat[y][x] == color:
                if a <= y and b <= x:
                    for i in range(a, y+1):
                        for j in range(b, x+1):
                            # print('ss', mat[i][j])
                            mat[i][j] = color
                else:
                    for i in range(y, a+1):
                        for j in range(x, b+1):
                            # print('ss', mat[i][j])
                            mat[i][j] = color

                # print('def', mat)
            break
        x = b
        y = a
        # print('cc', mat)
    # print('상하좌우 끝', mat)

    for i in range(4, 8):
        a = y
        b = x
        Y = a
        X = b
        cnt = 0
        # print('a, b', a, b)
        # print('Y, X', Y, X)
        while 0 <= x < N and 0 <= y < N:
            y += dy[i]
            x += dx[i]
            # print('y, x', y, x)
            if x == -1 or y == -1 or x == N or y == N:
                break
            elif mat[y][x] == 0:
                break
            elif mat[y][x] != color:
                # print('matvalue', mat[y][x])
                cnt += 1
                continue
            elif mat[y][x] == color:

                for c in range(cnt):
                    mat[a][b] = color
                    a += dy[i]
                    b += dx[i]
                    # print('change a, b', a, b)
                    mat[a][b] = color
                # print('대각선', mat)
            break
        y = Y
        x = X
    # print('대각선끝', mat)

    return mat



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    mat = [[0]*N for _ in range(N)]

    mat[N//2-1][N//2-1] = 2
    mat[N//2-1][N//2] = 1
    mat[N//2][N//2-1] = 1
    mat[N//2][N//2] = 2

    # print('1', mat)

    for m in range(M):
        x, y, color = map(int, input().split())
        # print(y, x)
        y = y-1
        x = x -1
        # print(y, x)
        mat[y][x] = color

        check(mat, x, y, color)
        # print('2', mat)
        # print('-------------------------------------')

    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                cnt1 += 1
            elif mat[i][j] == 2:
                cnt2 += 1

    print('#%d %d %d' % (tc, cnt1, cnt2))
    # print('res:', mat)






