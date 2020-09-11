# 다익스트라
# 완전검색 순열 만들어서도 풀 수 있음

import sys
sys.stdin = open('5251.txt', 'r')


# D: 출발점에서 각 정점까지 최단 경로 가중치 합을 저장
# P: 최단 경로 트리 저장
def dijkstra(G, r):  # r: 시작 정점
    D = [float('inf')] * (N+1)
    P = [None] * (N+1)
    visited = [0] * (N+1)  # 그래프 각 정점의 방문 여부
    D[r] = 0

    for _ in range(N+1):
        minidx = -1
        min = float('inf')
        for i in range(N+1):
            if not visited[i] and D[i] < min:
                min = D[i]
                minidx = i
        visited[minidx] = True
        for g in G[minidx]:
            v, val = g
            if not visited[v] and D[minidx] + val < D[v]:
                D[v] = D[minidx] + val
                P[v] = minidx
    return D

for tc in range(1, 1+int(input())):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        G[s].append((e, w))
    # print(arr)
    D = dijkstra(G, 0)
    print('#%d %d' % (tc, D[N]))
