import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    V, E = map(int, input().split())
    li = [[] for _ in range(V)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        li[v1-1].append(v2-1)
        li[v2 - 1].append(v1 - 1)

    flag = False

    for i in range(V):
        g1 = []
        g2 = []
        g1.append(i)
        for j in li[i]:
            g2.append(j)
        for v in g2:
            for k in li[v]:
                if k in g2:
                    print('NO')
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    else:
        print('YES')

    # arr = [[0]*V for _ in range(V)]
    #
    # for _ in range(E):
    #     v1, v2 = map(int, input().split())
    #     arr[v1-1][v2-1] = 1
    #     arr[v2-1][v1-1] = 1
    # print(arr)
    # flag = False
    #
    # for i in range(V):
    #     g1 = []
    #     g2 = []
    #     g1.append(i)
    #     for j in range(len(arr[i])):
    #         if arr[i][j]:
    #             g2.append(j)
    #     # print(g1, g2)
    #     for v in g2:
    #         # print('v', v)
    #         for k in range(len(arr[v])):
    #             if arr[v][k]:
    #                 if k in g2:
    #                     # print(k)
    #                     print('NO')
    #                     flag = True
    #                     break
    #             # print(g2)
    #         if flag:
    #             break
    #     if flag:
    #         break
    # else:
    #     print('YES')

