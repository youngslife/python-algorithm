import sys
sys.stdin = open("5201.txt", "r")

def check(w):
    global tW
    global res
    for i in range(len(tW)-1, -1, -1):
        if w <= tW[i]:
            res += w
            tW.pop(i)
            return


for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())))
    tW = sorted(list(map(int, input().split())))
    res = 0
    for i in range(len(w)-1, -1, -1):
        check(w[i])
    print('#%d %d'%(tc, res))