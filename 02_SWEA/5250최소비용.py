# 다익스트라
import sys
sys.stdin = open('5250.txt', 'r')

# D: 출발점에서 각 정점까지 최단 경로 가중치 합을 저장
# P: 최단 경로 트리 저장

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dijkstra(G, i, j):  # r: 시작 정점
    D = [[float('inf')] * N for _ in range(N)]
    P = [[None] * N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]  # 그래프 각 정점의 방문 여부
    D[i][j] = 0

    for _ in range(N*N):
        minidx = (-1, -1)
        min = float('inf')
        for ii in range(N):
            for jj in range(N):
                if not visited[ii][jj] and D[ii][jj] < min:
                    min = D[ii][jj]
                    minidx = (ii, jj)

        visited[minidx[0]][minidx[1]] = True

        for n in range(4):
            ii = minidx[0] + dy[n]
            jj = minidx[1] + dx[n]
            # print(ii, jj)
            if 0 <= ii < N and 0 <= jj < N:
                if H[ii][jj] > H[minidx[0]][minidx[1]]:
                    val = H[ii][jj] - H[minidx[0]][minidx[1]] + 1
                else:
                    val = 1

                if not visited[ii][jj] and D[minidx[0]][minidx[1]] + val < D[ii][jj]:
                    D[ii][jj] = D[minidx[0]][minidx[1]] + val
                    P[ii][jj] = minidx
    return D[N-1][N-1]

#
# def dijkstra(s, A):  # s: 시작 정점, A: 인접 행렬, D: 거리, V: 정점 집합
#     U = {s}  # U: 선택된 정점 집합
#
#     for n in range(4):


for tc in range(1, 1+int(input())):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    print('#%d %d' % (tc, dijkstra(H, 0, 0)))


