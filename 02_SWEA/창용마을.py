import sys
sys.stdin = open('2.txt', 'r')


def bfs(v):
    q = [v]
    visited[v] = 1
    while q:
        t = q.pop(0)
        if relation[t]:
            for e in relation[t]:
                if not visited[e]:
                    q.append(e)
                    visited[e] = 1


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    relation = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)

    visited = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            cnt += 1
    print('#%d %d' % (tc, cnt))