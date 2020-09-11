import sys
sys.stdin = open("4871.txt", "r")

for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())

    arr = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        print(a, b)
        arr[a][b] = 1

    print(arr)
