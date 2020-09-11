import sys
sys.stdin = open("5202.txt", "r")
from operator import itemgetter


def select(i, j):
    global cnt
    m = i + 1

    while m < j and table[m][0] < table[i][1]:
        m = m + 1

    if m < j:
        cnt += 1
        select(m, j)
        return
    else:
        return


for tc in range(1, 1+int(input())):
    N = int(input())
    table = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N)]
    table.sort(key=itemgetter(1))
    cnt = 0
    select(0, len(table))
    print('#%d %d'%(tc, cnt))