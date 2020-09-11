import sys
sys.stdin = open('input2.txt', 'r')

def dfs(i ,j):
    global check

    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1):
        Y = i + dy
        X = j + dx
        if 0 <= Y < N and 0 <= X < N:
            if type(arr[Y][X]) == int:
                if arr[Y][X] == 0:
                    arr[Y][X] = 'e'
                    dfs(Y, X)
                elif arr[Y][X] > 0:
                    check -= 1
                    arr[Y][X] = 'e'


for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    check = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                num = 0
                for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1):
                    Y = i + dy
                    X = j + dx
                    if 0 <= Y < N and 0 <= X < N:
                        if arr[Y][X] == '*':
                            num += 1
                if num > 0:
                    check += 1

                arr[i][j] = num

    click = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                dfs(i, j)
                click += 1

    print('#%d %d' % (tc, click+check))



