import sys
sys.stdin = open("5102.txt", "r")

def dfs(S):
    q = []
    q.append(S)
    distance[S] = 0

    while q:
        t = q.pop(0)

        if not visited[t]:
            visited[t] = True
            if t == G:
                result = distance[t]
                return result

        for i in range(len(arr[t])):
            if arr[t][i] == 1 and not visited[i]:
                q.append(i)
                if distance[i] == 0:  # 삼각지? 다 연결되어 있는 경우...2로 바뀔 수 있음..
                    distance[i] = distance[t] + 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        v1, v2 = map(int, input().split())
        arr[v1][v2] = 1
        arr[v2][v1] = 1

    S, G = map(int, input().split())


    visited = [0]*(V+1)
    distance = [0]*(V+1)

    result = dfs(S)

    print('#%d %d' % (tc, result))

    # q = []
    # q.append(S)
    # distance[S] = 0
    #
    # while q:
    #     t = q.pop(0)
    #
    #     if not visited[t]:
    #         visited[t] = True
    #         if t == G:
    #             result = distance[t]
    #             print('#%d %d' % (tc, result))
    #
    #     for i in range(len(arr[t])):
    #         if arr[t][i] == 1 and not visited[i]:
    #             q.append(i)
    #             distance[i] = distance[t] + 1
    # else:
    #     print('#%d %d' % (tc, 0))






