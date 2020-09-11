import sys
sys.stdin = open("input.txt", "r")

N, M, x, y, K = map(int, input().split())
geo = [list(map(int, input().split())) for _ in range(N)]
move = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if geo[i][j] == 0:
            start = (i, j)
            break