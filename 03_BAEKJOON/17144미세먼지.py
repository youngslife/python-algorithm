import sys
sys.stdin = open("input.txt", "r")

R, C, T = map(int, input().split())  # row, column, time
arr = [list(map(int, input().split())) for _ in range(R)]
cleaner = []

for i in range(2, R-2):
    if arr[i][0] == -1:
        cleaner.append(i)

for _ in range(T):
    # 미세먼지 확산
    temp = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                spread = arr[i][j] // 5
                cnt = 0
                for dy, dx in (-1, 0), (0, 1), (1, 0), (0, -1):
                    if 0 <= i + dy < R and 0 <= j + dx < C and arr[i+dy][j+dx] >= 0:
                        temp[i+dy][j+dx] += spread
                        cnt += 1
                temp[i][j] -= spread * cnt

    for i in range(R):
        for j in range(C):
            arr[i][j] += temp[i][j]

    # 공기청정 1
    temp1 = [[0]*C for _ in range(R)]
    for j in range(C-1):
        if arr[cleaner[0]][j] > 0:
            temp1[cleaner[0]][j+1] = arr[cleaner[0]][j]
    for k in range(cleaner[0], 0, -1):
        if arr[k][C-1] > 0:
            temp1[k-1][C-1] = arr[k][C-1]
    for j in range(C-1, 0, -1):
        if arr[0][j] > 0:
            temp1[0][j-1] = arr[0][j]
    for k in range(cleaner[0]-1):
        if arr[k][0] > 0:
            temp1[k+1][0] = arr[k][0]

    # 공기 청정 2
    for j in range(C-1):
        if arr[cleaner[1]][j] > 0:
            temp1[cleaner[1]][j+1] = arr[cleaner[1]][j]
    for k in range(cleaner[1], R-1):
        if arr[k][C-1] > 0:
            temp1[k+1][C-1] = arr[k][C-1]
    for j in range(C - 1, 0, -1):
        if arr[R-1][j] > 0:
            temp1[R-1][j - 1] = arr[R-1][j]
    for k in range(R-1, cleaner[1], -1):
        if arr[k][0] > 0:
            temp1[k-1][0] = arr[k][0]

    res = 0

    for i in range(R):
        for j in range(C):
            if i == 0 or i == cleaner[0] or i == cleaner[1] or i == R-1 or j == 0 or j == C-1:
                if arr[i][j] == -1:
                    continue
                arr[i][j] = temp1[i][j]
            res += arr[i][j]

print(res)


