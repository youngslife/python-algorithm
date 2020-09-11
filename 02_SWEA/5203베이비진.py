import sys
sys.stdin = open("5203.txt", "r")

import sys
sys.stdin = open("5203.txt", "r")

def perm1(n, k, li):
    global res
    if k == n:
        for i in range(6):
            if int(li[i])+2 == int(li[i+1]) + 1 == int(li[i+2]):
                res = 1
                return
            elif int(li[i]) == int(li[i+1]) == int(li[i+2]):
                res = 1
                return
            else:
                return
        return
    else:
        for i in range(k, n):
            li[k], li[i] = li[i], li[k]
            perm1(n, k+1, li)
            li[k], li[i] = li[i], li[k]


def perm2(n, k, li):
    global res
    if k == n:
        for i in range(6):
            if int(li[i])+2 == int(li[i+1]) + 1 == int(li[i+2]):
                res = 2
                return
            elif int(li[i]) == int(li[i+1]) == int(li[i+2]):
                res = 2
                return
            else:
                return
        return
    else:
        for i in range(k, n):
            li[k], li[i] = li[i], li[k]
            perm2(n, k+1, li)
            li[k], li[i] = li[i], li[k]


for tc in range(1, 1+int(input())):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []
    res = 0
    for i in range(0, 12, 2):
        p1.append(cards[i])
        p2.append(cards[i+1])

    for i in range(3, 7):
        perm1(i, 0, p1[:i])
        if res == 1:
            break
        perm2(i, 0, p2[:i])
        if res == 2:
            break

    print('#%d %d'%(tc, res))


