# 입력값으로 그래프 만들고 최소신장 트리 알고리즘 사용

import sys
sys.stdin = open('5249.txt', 'r')

# def Make_set(x):  # 유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산
#     p[x] = x  # 노드 x의 부모 저장
#     rank[x] = 0  # 루트 노드가 x인 트리의 랭크 값 저장
#
#
# def Find_Set(x):  # x를 포함하는 집합을 찾는 연산
#     if x != p[x]:
#         p[x] = Find_Set(p[x])
#     return p[x]
#
# def Union(x, y):  # x, y를 포함하는 두 집합을 통합하는 연산
#     p[Find_Set(y)] = Find_Set(x)
#
#
# def kruskal(G):
#     mst = []  # 간선들의 트리
#
#     for i in range(N):
#         Make_set(i)
#
#     G.sort(key=lambda t: t[2])  # 가중치 기준으로 정렬
#
#     mst_cost = 0  # MST 가중치
#
#     while len(mst) < N-1:
#         u, v, val = G.pop(0)  # 최소 가중치 간선 가져오기
#         if Find_Set(u) != Find_Set(v):
#             Union(u, v)
#             mst.append((u, v))
#             mst_cost += val


def prim(G, s):  # G: 그래프, s: 시작 정점
    key = [float('inf')] * (V+1)  # 가중치를 무한대로 초기화
    pi = [None]*(V+1)  # 트리에서 연결될 부모 정점 초기화
    # print(pi)
    visited = [0]*(V+1)  # 방문여부 초기화
    key[s] = 0  # 시작 정점의 가중치를 0으로 설정
    # print(key)

    for _ in range(V+1):  # 정점의 개수만큼 반복
        minidx = -1
        min = float('inf')
        for i in range(V+1):  # 방문 안한 정점중 최소 가중치 정점 찾기
            if not visited[i] and key[i] < min:
                min = key[i]
                minidx = i

        visited[minidx] = 1  # 최소 가중치 정점 방문처리

        for g in G[minidx]:  # 선택 정점의 인접한 정점
            v, val = g
            if not visited[v] and val < key[v]:
                key[v] = val  # 가중치 갱신
                pi[v] = minidx  # 트리에서 연결될 부모 정점
    return(sum(key))


for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())
    G = [[]*(V + 1) for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        G[a].append((b, c))
        G[b].append((a, c))
    # print(G)
    print('#%d %d' % (tc, prim(G, 0)))
