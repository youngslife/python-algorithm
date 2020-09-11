import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
value = [int(input()) for _ in range(N)]

cnt = 0
for v in range(len(value)-1, -1, -1):
    if K >= value[v]:
        while K >= value[v]:
            K -= value[v]
            cnt += 1

print(cnt)

# 117732 KB / 300ms

