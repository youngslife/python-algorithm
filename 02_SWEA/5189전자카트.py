import sys
sys.stdin = open("5189.txt", "r")
# 완전검색

def perm(k):
    global res
    if k == len(li):
        line = [0] + li + [0]
        total = 0
        for i in range(len(line)-1):
            total += arr[line[i]][line[i+1]]
        if res > total:
            res = total
        return

    else:
        for i in range(k, len(li)):
            li[k], li[i] = li[i], li[k]
            perm(k+1)
            li[k], li[i] = li[i], li[k]


for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    li = [i for i in range(1, N)]
    res = 100**10
    perm(0)
    print('#%d %d' % (tc, res))
