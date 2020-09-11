import sys
sys.stdin = open("input4837.txt", "r")

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())  # N=부분집합원소개수, k= 합
    count = 0

    for i in range(1 << len(A)):
        sub = []
        t = 0
        for j in range(len(A)):
            if i & (1 << j):
                sub.append(j)
                t += A[j]

        if len(sub) == N:
            if t == K:
                count += 1

    print('#%d %d' % (tc, count))
