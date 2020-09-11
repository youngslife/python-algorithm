import sys
sys.stdin = open('input.txt', 'r')

def right(i, j):
    y, x = i, j
    while True:
         x += 1
         if 0 <= x < M:
            if arr[y][x] == 0:
                arr[y][x] = 7
            elif arr[y][x] == 6:
                break
            else:
                continue
         else:
             break

def left(i, j):
    y, x = i, j
    while True:
         x += -1
         if 0 <= x < M:
            if arr[y][x] == 0:
                arr[y][x] = 7
            elif arr[y][x] == 6:
                break
         else:
             break

def up(i, j):
    y, x = i, j
    while True:
        y -= 1
        if 0 <= y < N:
            if arr[y][x] == 0:
                arr[y][x] = 7
            elif arr[y][x] == 6:
                break
        else:
            break

def down(i, j):
    y, x = i, j
    while True:
        y += 1
        if 0<= y < N:
            if arr[y][x] == 0:
                arr[y][x] = 7
            elif arr[y][x] == 6:
                break
        else:
            break

###########################################

def H(k):
    global cnt
    global arr

    temp = [[0]*M for _ in range(N)]
    for tx in range(N):
        for ty in range(M):
            temp[tx][ty] = arr[tx][ty]

    if k == len(cctv):
        check = 0
        for idx in range(len(dirs)):
            if cctv[idx][0] == 1:
                if dirs[idx] == 0:
                    right(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 1:
                    left(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 2:
                    up(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 3:
                    down(cctv[idx][1], cctv[idx][2])
            elif cctv[idx][0] == 2:
                if dirs[idx] == 0 or dirs[idx] == 2:
                    right(cctv[idx][1], cctv[idx][2])
                    left(cctv[idx][1], cctv[idx][2])
                else:
                    up(cctv[idx][1], cctv[idx][2])
                    down(cctv[idx][1], cctv[idx][2])
            elif cctv[idx][0] == 3:
                if dirs[idx] == 0:
                    up(cctv[idx][1], cctv[idx][2])
                    right(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 1:
                    right(cctv[idx][1], cctv[idx][2])
                    down(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 2:
                    down(cctv[idx][1], cctv[idx][2])
                    left(cctv[idx][1], cctv[idx][2])
                else:
                    left(cctv[idx][1], cctv[idx][2])
                    up(cctv[idx][1], cctv[idx][2])
            elif cctv[idx][0] == 4:
                if dirs[idx] == 0:
                    left(cctv[idx][1], cctv[idx][2])
                    up(cctv[idx][1], cctv[idx][2])
                    right(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 1:
                    up(cctv[idx][1], cctv[idx][2])
                    right(cctv[idx][1], cctv[idx][2])
                    down(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 2:
                    right(cctv[idx][1], cctv[idx][2])
                    down(cctv[idx][1], cctv[idx][2])
                    left(cctv[idx][1], cctv[idx][2])
                else:
                    down(cctv[idx][1], cctv[idx][2])
                    left(cctv[idx][1], cctv[idx][2])
                    up(cctv[idx][1], cctv[idx][2])

        for y in range(N):
            for x in range(M):
                if arr[y][x] == 0:
                    check += 1
        if check < cnt:
            cnt = check
        arr = temp

    else:
        for d in range(4):
            dirs[k] = d
            H(k+1)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cctv = []
cnt = 0

for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 5:
            cctv.append((arr[i][j], i, j))
        elif arr[i][j] == 5:
            right(i, j)
            left(i, j)
            up(i, j)
            down(i, j)
        elif arr[i][j] == 0:
            cnt += 1

dirs = [0] * len(cctv)
H(0)
print(cnt)

# 124244KB / 728ms

#####################
# def check():

def H(k, s):
    global cnt
    global arr

    temp = copy.deepcopy(arr)
    if k == len(cctv):
        check = 0
        for idx in range(len(dirs)):
            if cctv[idx][0] == 1:
                if dirs[idx] == 0:
                    right(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 1:
                    left(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 2:
                    up(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 3:
                    down(cctv[idx][1], cctv[idx][2])
            elif cctv[idx][0] == 2:
                if dirs[idx] == 0 or dirs[idx] == 2:
                    right(cctv[idx][1], cctv[idx][2])
                    left(cctv[idx][1], cctv[idx][2])
                else:
                    up(cctv[idx][1], cctv[idx][2])
                    down(cctv[idx][1], cctv[idx][2])
            elif cctv[idx][0] == 3:
                if dirs[idx] == 0:
                    up(cctv[idx][1], cctv[idx][2])
                    right(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 1:
                    right(cctv[idx][1], cctv[idx][2])
                    down(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 2:
                    down(cctv[idx][1], cctv[idx][2])
                    left(cctv[idx][1], cctv[idx][2])
                else:
                    left(cctv[idx][1], cctv[idx][2])
                    up(cctv[idx][1], cctv[idx][2])
            elif cctv[idx][0] == 4:
                if dirs[idx] == 0:
                    left(cctv[idx][1], cctv[idx][2])
                    up(cctv[idx][1], cctv[idx][2])
                    right(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 1:
                    up(cctv[idx][1], cctv[idx][2])
                    right(cctv[idx][1], cctv[idx][2])
                    down(cctv[idx][1], cctv[idx][2])
                elif dirs[idx] == 2:
                    right(cctv[idx][1], cctv[idx][2])
                    down(cctv[idx][1], cctv[idx][2])
                    left(cctv[idx][1], cctv[idx][2])
                else:
                    down(cctv[idx][1], cctv[idx][2])
                    left(cctv[idx][1], cctv[idx][2])
                    up(cctv[idx][1], cctv[idx][2])

        print('arr', arr)

        for y in range(N):
            for x in range(M):
                if arr[y][x] == 0:
                    check += 1
        if check < cnt:
            cnt = check

        arr = temp
        print('temp', temp)
        return

    else:
        for i in range(s, len(cctv)):
            for d in range(4):
                dirs[i] = d
                H(k+1, i)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cctv = []
cnt = 0

for i in range(N):
    for j in range(M):
        if 0 < arr[i][j] < 5:
            cctv.append((arr[i][j], i, j))
        elif arr[i][j] == 5:
            right(i, j)
            left(i, j)
            up(i, j)
            down(i, j)
        elif arr[i][j] == 0:
            cnt += 1

print(cctv)
print(arr)
dirs = [0] * len(cctv)
H(0, 0)
print(cnt)




# 중복조합코드
# def H(k, s):
#     if k == R:
#         print(t[0], t[1])
#     else:
#         for i in range(s, N):
#             t[k] = a[i]
#             H(k+1, i)
#
#
# N = 3
# R = 2
# a = [1, 2, 3]
# t = [0] * R
# H(0, 0)



