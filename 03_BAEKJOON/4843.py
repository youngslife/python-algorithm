import sys
sys.stdin = open("input4843.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    for i in range(N-1):
        if i % 2:
            m = i
            for j in range(i+1, N):
                if ai[m] > ai[j]:
                    m = j
            ai[i], ai[m] = ai[m], ai[i]
        else:
            M = i
            for j in range(i+1, N):
                if ai[M] < ai[j]:
                    M = j
            ai[i], ai[M] = ai[M], ai[i]

    result = str(ai[:10])[1:-1].replace(',', '')

    print('#%d %s' % (tc, result))
