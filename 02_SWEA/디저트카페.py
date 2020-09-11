import sys
sys.stdin = open('input1.txt', 'r')

dy = [1, 1, -1, -1]
dx = [1, -1, -1, 1]

def dfs(y, x, d, cnt, dessert):
    global stop, res
    #
    # if cnt > 0:
    #     # print(cnt)
    #     if stop == (y, x):
    #         if res < cnt:
    #             res = cnt + 1
    #             return

    if d == 0:
        if 0 <= y+dy[0] < N and 0 <= x+dx[0] < N:
            if cafes[y+dy[0]][x+dx[0]] not in dessert:
                dfs(y+dy[0], x+dx[0], 0, cnt+1, dessert+[cafes[y+dy[0]][x+dx[0]]])
        if 0 <= y + dy[1] < N and 0 <= x + dx[1] < N:
            if cafes[y+dy[1]][x+dx[1]] not in dessert:
                dfs(y+dy[1], x+dx[1], 1, cnt+1, dessert+[cafes[y+dy[1]][x+dx[1]]])
    elif d == 1:
        if 0 <= y + dy[1] < N and 0 <= x + dx[1] < N:
            if cafes[y+dy[1]][x+dx[1]] not in dessert:
                dfs(y+dy[1], x+dx[1], 1, cnt+1, dessert+[cafes[y+dy[1]][x+dx[1]]])
        if 0 <= y + dy[2] < N and 0 <= x + dx[2] < N:
            if cafes[y+dy[2]][x+dx[2]] not in dessert:
                dfs(y+dy[2], x+dx[2], 2, cnt+1, dessert+[cafes[y+dy[2]][x+dx[2]]])

    elif d == 2:
        if 0 <= y + dy[2] < N and 0 <= x + dx[2] < N:
            if cafes[y+dy[2]][x+dx[2]] not in dessert:
                dfs(y+dy[2], x+dx[2], 2, cnt+1, dessert+[cafes[y+dy[2]][x+dx[2]]])
        if 0 <= y + dy[3] < N and 0 <= x + dx[3] < N:
            if cafes[y+dy[3]][x+dx[3]] not in dessert:
                dfs(y+dy[3], x+dx[3], 3, cnt+1, dessert+[cafes[y+dy[3]][x+dx[3]]])
            else:
                if stop == (y + dy[3], x + dx[3]):
                    if res < cnt:
                        res = cnt + 1
                        return

    elif d == 3:
        if 0 <= y + dy[3] < N and 0 <= x + dx[3] < N:
            if cafes[y+dy[3]][x+dx[3]] not in dessert:
                dfs(y+dy[3], x+dx[3], 3, cnt+1, dessert+[cafes[y+dy[3]][x+dx[3]]])
            else:
                if stop == (y + dy[3], x + dx[3]):
                    if res < cnt:
                        res = cnt + 1
                        return
        # if 0 <= y + dy[0] < N and 0 <= x + dx[0] < N:
        #     if cafes[y][x] != cafes[y+dy[0]][x+dx[0]]:
        #         dfs(y+dy[0], x+dx[0], 0, cnt+1)



for tc in range(1, 1+int(input())):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for i in range(N-1):
        for j in range(1, N-1):
            stop = (i, j)
            dfs(i, j, 0, 0, [cafes[i][j]])

    if res == 0:
        res = -1

    print('#%d %d' % (tc, res))