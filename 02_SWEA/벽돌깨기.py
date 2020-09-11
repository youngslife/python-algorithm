import sys
sys.stdin = open('input2.txt', 'r')

def shoot(i, j, power, temp):
    # print(i, j)
    temp[i][j] = 0
    uy, ux = i, j
    by, bx = i, j
    ly, lx = i, j
    ry, rx = i, j

    for _ in range(power-1):
        uy, ux = uy - 1, ux
        if 0 <= uy < H and 0 <= ux < W and temp[uy][ux] > 0:
            shoot(uy, ux, temp[uy][ux], temp)

        by, bx = by + 1, bx
        if 0 <= by < H and 0 <= bx < W and temp[by][bx] > 0:
            shoot(by, bx, temp[by][bx], temp)

        ly, lx = ly, lx - 1
        if 0 <= ly < H and 0 <= lx < W and temp[ly][lx] > 0:
            shoot(ly, lx, temp[ly][lx], temp)

        ry, rx = ry, rx + 1
        if 0 <= ry < H and 0 <= rx < W and temp[ry][rx] > 0:
            shoot(ry, rx, temp[ry][rx], temp)
    return temp

def down(temp):
    for i in range(H-2, -1, -1):
        for j in range(W-1, -1, -1):
            if temp[i][j]:
                y, x = i, j
                flag = True
                while flag:
                    y += 1
                    if 0 <= y < H:
                        if temp[y][x]:
                            flag = False
                    else:
                        flag = False
                temp[y-1][x] = temp[i][j]
                if y-1 != i:
                    temp[i][j] = 0
    return temp






# 중복순열
def perm(k):
    global mini
    if k == N:
        # print(spot)

        temp = [[0]*W for _ in range(H)]
        for tx in range(H):
            for ty in range(W):
                temp[tx][ty] = arr[tx][ty]

        for x in spot:
            for y in range(H):
                if temp[y][x]:
                    temp = shoot(y, x, temp[y][x], temp)
                    # print(temp)
                    temp = down(temp)
                    break
        # print('---------------------')

        res = 0
        for i in range(H):
            for j in range(W):
                if temp[i][j]:
                    res += 1

        # print('res', res)
        # print('_________________------')
        if res < mini:
            mini = res


    else:
        for i in range(W):
            spot[k] = w_spot[i]
            perm(k+1)

for tc in range(1, 1+int(input())):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    w_spot = [x for x in range(W)]  # 굳이 안해줘도 될것 같긴 해요
    spot = [0]*N
    mini = 10000000000000000000000000
    # print(w_spot)
    # print(spot)
    # print('arr', arr)
    perm(0)
    print('#%d %d' % (tc, mini))


