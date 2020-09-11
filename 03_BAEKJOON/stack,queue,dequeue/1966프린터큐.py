import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    ipts = list(map(int, input().split()))
    idx = 0
    i = -1
    res = 0
    while True:
        i = (i + 1) % len(ipts)
        if ipts[i]:
            for j in range(len(ipts)):
                if j != i:
                    if ipts[j] > ipts[i]:
                        break
            else:
                idx += 1
                ipts[i] = 0
                if i == M:
                    print(idx)
                    break

# pypy3:  117940 KB / 128 ms
# python3:  29056 KB / 92 ms
