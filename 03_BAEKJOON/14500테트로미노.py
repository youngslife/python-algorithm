import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# dfs 로 4칸의 합의 최대
ans = 0

def dfs(i, j, n, sum):
    global ans

    if n == 4:
        if sum > ans:
            ans = sum
        return

    for dy, dx in (0, 1), (1, 0), (0, -1), (-1, 0):
        if 0 <= i+dy < N and 0 <= j + dx < M and not visited[i+dy][j+dx]:
            visited[i+dy][j+dx] = 1
            dfs(i+dy, j+dx, n+1, sum+arr[i+dy][j+dx])
            visited[i+dy][j+dx] = 0


def exceptCase(i, j, n, sum):
    global ans

    if n == 4:
        if sum > ans:
            ans = sum
            return

    for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
        if 0 <= i + di < N and 0 <= j + dj < M and not visited[i + di][j + dj]:
            visited[i+di][j+dj] = 1
            exceptCase(i, j, n+1, sum+arr[i+di][j+dj])
            visited[i+di][j+dj] = 0

visited = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        #visited = [[0] * M for _ in range(N)]
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        #visited = [[0] * M for _ in range(N)]
        # visited[i][j] = 1
        exceptCase(i, j, 1, arr[i][j])
        visited[i][j] = 0
        # if 0 < i < N-1 and 0 < j < M-1:
        #     temps = [
        #         arr[i][j] + arr[i][j - 1] + arr[i - 1][j] + arr[i][j + 1],
        #         arr[i][j] + arr[i - 1][j] + arr[i][j + 1] + arr[i + 1][j],
        #         arr[i][j] + arr[i][j + 1] + arr[i + 1][j] + arr[i][j - 1],
        #         arr[i][j] + arr[i + 1][j] + arr[i][j - 1] + arr[i - 1][j]
        #     ]
        #
        #     for temp in temps:
        #         if temp > ans:
        #             ans = temp

print(ans)