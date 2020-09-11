import sys
sys.stdin = open("5178.txt", "r")

for tc in range(1, 1+int(input())):
    N, M, L = map(int, input().split())

    li = [0]*(N+1)

    for i in range(M):
        idx, v = map(int, input().split())
        li[idx] = v

    if len(li) % 2:
        for i in range(len(li)//2, -1, -1):
            if i == len(li)//2:
                li[i] = li[2*i]
            else:
                li[i] = li[2 * i] + li[2 * i + 1]
    else:
        for i in range(len(li) // 2 - 1, -1, -1):
            li[i] = li[2 * i] + li[2 * i + 1]

    print('#%d %d'%(tc, li[L]))
