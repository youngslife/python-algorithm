import sys
sys.stdin = open('input.txt', 'r')

def bfs(y, x):
    global size, arr, time
    q = [(y, x)]
    visited = [[0]*N for _ in range(N)]
    # visited[y][x] = 1
    eat = 0

    flag = False
    while q:
        y, x = q.pop(0)
        # visited[y][x] = 1

        for dy, dx in (-1, 0), (0, -1), (1, 0), (0, 1):
            Y = y + dy
            X = x + dx
            if 0 <= Y < N and 0 <= X < N and arr[Y][X] <= size:
                if 0 < arr[Y][X] < size:
                    eat += 1
                    arr[Y][X] = 0
                    q.append((Y, X))
                    visited[Y][X] += visited[y][x] + 1
                    time += visited[Y][X]
                    # print('time', time)
                    visited = [[0]*N for _ in range(N)]
                    q = [(Y, X)]
                    if eat == size:
                        size += 1
                        eat = 0
                    print(Y, X, size)
                    break
                elif arr[Y][X] == size:
                    q.append((Y, X))
                    visited[Y][X] += visited[y][x] + 1
                elif arr[Y][X] == 0:
                    q.append((Y, X))
                    visited[Y][X] += visited[y][x] + 1
        print('t', time)
        print(time, q)
        again = False
        for i in range(N):
            for j in range(N):
                if 0 < arr[i][j] < size:
                    again = True
                    break
            if again:
                break
        else:
            break





N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

size = 2
time = 0

start = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            y, x = i, j
            arr[i][j] = 0  # 지나갈 수 있도록 상어 자리 0으로
        elif 0 < arr[i][j] < size:
            start = True
            continue

if start:
    bfs(y, x)
else:
    print(0)
