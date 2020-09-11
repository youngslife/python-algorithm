import sys
sys.stdin = open('5209.txt', 'r')


def perm(k, s):
    global res
    if s > res:
        return

    if k == N:
        tsum = 0
        for i in range(N):
            tsum += arr[i][t[i]]
        if tsum < res:
            res = tsum
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = i
            visited[i] = 1
            perm(k + 1, s + arr[k][i])
            visited[i] = 0


for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 99*N
    t = [0]*N
    visited = [0]*N
    perm(0,0)
    print('#%d %d'%(tc, res))

