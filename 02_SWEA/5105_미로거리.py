import sys
sys.stdin = open("5105.txt", "r")

dx = [0, 0, -1, 1]  # 상 하 좌 우
dy = [-1, 1, 0, 0]
def isWall(y, x):
    if x < 0 or x >= N:
        return True
    if y < 0 or y >= N:
        return True
    return False

# def IsSafe(y,x):
#     return 0 <= y < N and 0<= x < N and (mat[y][x] == 0 or mat[y][x] == 3)

def bfs(s1, s2):
    q.append((s1, s2))

    while q:
        y, x = q.pop(0)
        for i in range(4):
            Y = y + dy[i]
            X = x + dx[i]
            if not isWall(Y, X) and not visited[Y][X] and (mat[Y][X] == 0 or mat[Y][X] == 3):
            # if IsSafe(Y, X) and not visited[Y][X]:
                visited[Y][X] = True
                q.append((Y, X))
                distance[Y][X] = distance[y][x] + 1
                if mat[Y][X] == 3:
                    result = distance[Y][X] -1
                    return result
    return 0

            # for i in 인접:
            #     if not visited[i]:
            #         q.append(i)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if mat[y][x] == 2:
                sY, sX = y, x

    q = []
    visited = [[0]*N for _ in range(N)]
    distance = [[0]*N for _ in range(N)]
    result = bfs(sY, sX)
    print(result)

