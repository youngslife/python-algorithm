import sys
sys.stdin = open("5176.txt", "r")

def traverse(T):
    global n
    global result
    if T:
        traverse(tree[T][0])
        n += 1
        result[T] = n
        # print(n)
        traverse(tree[T][1])

for tc in range(1, 1+int(input())):
    N = int(input())

    tree = [[0]*2 for _ in range(N+1)]

    for i in range(1, N//2+1):
        tree[i][0] = 2*i
        if not N % 2:
            if i < N//2:
                tree[i][1] = 2*i + 1
        else:
            tree[i][0], tree[i][1] = 2*i, 2*i + 1

    n = 0
    result = [0]*(N+1)
    print(tree)

    traverse(1)
    print(result)

    print('#%d %d %d'%(tc, result[1], result[N//2]))







