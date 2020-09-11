import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))



