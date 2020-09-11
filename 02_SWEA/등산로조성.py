import sys
sys.stdin = open('input2.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x, V, cnt, used):
    global res

    visited[y][x] = 1
    for n in range(4):
        Y = y + dy[n]
        X = x + dx[n]
        if 0 <= Y < N and 0 <= X < N and not visited[Y][X]:
            if arr[Y][X] < V:
                dfs(Y, X, arr[Y][X], cnt + 1, used)
            else:
                if not used:
                    for k in range(1, K+1):
                        value = arr[Y][X] - k
                        if value < V:
                            used = True
                            dfs(Y, X, value, cnt + 1, used)
                            used = False

    visited[y][x] = 0
    if cnt > res:
        res = cnt



for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxh = 0
    highests = []

    for y in range(N):
        for x in range(N):
            if arr[y][x] > maxh:
                maxh = arr[y][x]
                highests = []
                highests.append((y, x))
            elif arr[y][x] == maxh:
                highests.append((y, x))
    # print(maxh)
    # print(highests)
    res = 0

    visited = [[0]*N for _ in range(N)]
    used = False
    for y, x in highests:
        dfs(y, x, arr[y][x], 1, used)


    print('#%d %d' % (tc, res))



