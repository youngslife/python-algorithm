import sys
sys.stdin = open('input3.txt', 'r')


def bfs(t):
    global visited
    y, x, value = t
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        Y = y + dy
        X = x + dx
        if 0 <= Y < R and 0 <= X < C and not visited[Y][X]:
            visited[Y][X] = 1
            arr[Y][X] = value




for tc in range(1, 1+int(input())):
    N, M, K = map(int, input().split())
    arr = [[0]*K + list(map(int, input().split())) + [0]*K for _ in range(N)]
    arr = [[0]*(K+M+K) for _ in range(K)] + arr + [[0]*(K+M+K) for _ in range(K)]
    time = 1
    visited = [[0]*len(arr[0]) for _ in range(len(arr))]
    temp = []
    R = len(arr)
    C = len(arr[0])
    # print(arr)

    while time < K:
        # print(arr)
        for i in range(R):
            for j in range(C):
                if arr[i][j]:
                    visited[i][j] = 1
                    if arr[i][j] == time - 1:
                        # print(time, i, j, arr[i][j])
                        temp.append((i, j, time + arr[i][j]))
                        arr[i][j] = - (time + arr[i][j])

                    elif arr[i][j] == - (time - 1):
                        # print('die', time, i, j, arr[i][j])
                        arr[i][j] = 0

        temp.sort()

        if temp:
            for t in temp:
                bfs(t)
        time += 1

    res = 0
    for i in range(R):
        for j in range(R):
            if arr[i][j]:
                res += 1
    print(res)




