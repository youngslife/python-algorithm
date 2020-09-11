import sys
sys.stdin = open('5248.txt', 'r')

def bfs(v):
    q = [v]
    visited[v] = 1
    while q:
        t = q.pop(0)
        for w in range(len(arr[t])):
            if arr[t][w]:
                if not visited[w]:
                    q.append(w)
                    visited[w] = 1

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    info = list(map(int, input().split()))
    for i in range(0, len(info), 2):
        arr[info[i]][info[i+1]] = 1
        arr[info[i+1]][info[i]] = 1

    res = 0
    visited = [0]*(N+1)
    for i in range(1, N+1):
        if not visited[i]:
            bfs(i)
            res += 1

    print('#%d %d' % (tc, res))


# 5만큼 makeset해놓고 1.2.3.들어오면 union set?
# disjoint set 써서 풀어도됨