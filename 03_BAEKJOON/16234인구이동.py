import sys
sys.stdin = open('input.txt', 'r')


def dfs(y, x, v):
    global arr, visited, end
    s = [(y, x)]
    populations = [arr[y][x]]
    place = [(y, x)]
    while s:
        y, x = s.pop(-1)
        visited[y][x] = 0
        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
            yy = y + dy
            xx = x + dx
            if 0 <= yy < N and 0 <= xx < N and visited[yy][xx] == v:
                s.append((yy, xx))
                populations.append(arr[yy][xx])
                place.append((yy, xx))
                visited[yy][xx] = 0
    print(s)
    print(populations)
    print(place)

    new = sum(populations) // len(populations)
    print(new)

    for i, j in place:
        arr[i][j] = new

    print('dfe', arr)

    for i in range(N):
        for j in range(N):
            for dy, dx in (0, 1), (1, 0):
                ii = i + dy
                jj = j + dx
                print(ii, jj)
                if 0 <= ii < N and 0 <= jj <= N:
                    if L <= arr[i][j] - arr[ii][jj] <= R or L <= arr[ii][jj] - arr[i][j] <= R:
                        print('rrr')
                        end = False
                        break
                    if end:
                        break
                if end:
                    break
            if end:
                break
        else:
            end = True


    print(arr)


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

end = False
cnt = 0

while not end:
    print('in')
    visited = [[0]*N for _ in range(N)]
    print(visited)
    v = 1
    print('new', arr)
    for i in range(N):
        for j in range(N):
            for dy, dx in (0, 1), (1, 0):
                ii = i + dy
                jj = j + dx
                if 0 <= ii < N and 0 <= jj < N:
                    if L <= arr[i][j] - arr[ii][jj] <= R or L <= arr[ii][jj] - arr[i][j] <= R:
                        if not visited[i][j]:
                            visited[i][j] = v
                            visited[ii][jj] = v
                            v += 1
                        else:
                            visited[ii][jj] = visited[i][j]
            # print(visited)

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                dfs(i, j, visited[i][j])
    cnt += 1

    print(arr)





print('res', cnt)



