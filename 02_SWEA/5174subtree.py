import sys
sys.stdin = open("5174.txt", "r")

def traverse(T):
    global cnt
    if T:
        cnt += 1
        for i in tree[T]:
            traverse(i)


for tc in range(1, 1+int(input())):
    E, N = map(int, input().split())

    tree = [[] for _ in range(E+2)]

    info = list(map(int, input().split()))

    for i in range(E):
        parent, child = info[2*i], info[2*i + 1]
        tree[parent].append(child)

    cnt = 0

    traverse(N)
    print('#%d %d'%(tc, cnt))

