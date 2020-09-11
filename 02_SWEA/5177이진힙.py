import sys
sys.stdin = open("5177.txt", "r")

for tc in range(1, 1+int(input())):
    N = int(input())
    tree = [0]*(N+1)

    li = list(map(int, input().split()))

    for i in range(N):
        tree[i+1] = li[i]
        if i > 0:
            while True:
                if tree[(i+1)//2] > tree[i+1]:
                    tree[(i+1)//2], tree[i+1] = tree[i+1], tree[(i+1)//2]
                else:
                    break
                i = (i+1)//2 - 1
    print(tree)

    res = 0
    n = len(tree)-1

    while n > 1:
        res += tree[n//2]
        n = n // 2

    print('#%d %d'%(tc, res))

