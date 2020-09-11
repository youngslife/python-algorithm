def bfs(v):
    global cnt
    q = []
    q.append(v)
    while q:
        v = q.pop(0)
        if not visited[v]:
            visited[v] = 1

            for w in arr[v]:
                if not visited[w]:
                    q.append(w)
                    visited[w] = 1
                    cnt += 1
        for i in q:
            for w in arr[i]:
                if not visited[w]:
                    visited[w] = 1
                    cnt += 1
        break


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    arr = [[] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    cnt = 0
    visited = [0] * (N + 1)
    bfs(1)
    print('#%d %d' % (tc, cnt))