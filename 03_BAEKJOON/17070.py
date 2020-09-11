import sys
sys.stdin = open('input.txt', 'r')

# 오른쪽, 아래, 대각선(0, 1, 2)
dy = [0, 1, 1]
dx = [1, 0, 1]

def backtrack(d, y, x):
    global cnt

    if y == N-1 and x == N-1:
        cnt += 1
        return

    if d == 0:
        Y = y + 0
        X = x + 1
        if 0 <= Y < N and 0 <= X < N:
            if home[Y][X] == 0:
                backtrack(0, Y, X)
            else:
                return

        Y = y + 1
        X = x + 1
        if 0 <= Y < N and 0 <= X < N and 0 <= x+1 < N and 0 <= y+1 < N:
            if home[Y][X] == 0 and home[y][x + 1] == 0 and home[y + 1][x] == 0:
                backtrack(2, Y, X)

    elif d == 1:
        Y = y + 1
        X = x + 1
        if 0 <= Y < N and 0 <= X < N:
            if home[Y][X] == 0 and home[y][x + 1] == 0 and home[y + 1][x] == 0:
                backtrack(2, Y, X)

        Y = y + 1
        X = x + 0
        if 0 <= Y < N and 0 <= X < N and 0 <= x+1 < N and 0 <= y+1 < N:
            if home[Y][X] == 0 and home[y][x + 1] == 0 and home[y + 1][x] == 0:
                backtrack(1, Y, X)


    elif d == 2:

        Y = y + 1
        X = x + 1
        if 0 <= Y < N and 0 <= X < N and 0 <= x+1 < N and 0 <= y+1 < N:
            if home[Y][X] == 0 and home[y][x + 1] == 0 and home[y + 1][x] == 0:
                backtrack(2, Y, X)

        Y = y + 0
        X = x + 1
        if 0 <= Y < N and 0 <= X < N:
            if home[Y][X] == 0:
                backtrack(0, Y, X)

        Y = y + 1
        X = x + 0
        if 0 <= Y < N and 0 <= X < N:
            if home[Y][X] == 0 and home[y][x + 1] == 0 and home[y + 1][x] == 0:
                backtrack(1, Y, X)




N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
backtrack(0, 0, 1)
print(cnt)