import sys
sys.stdin = open("1493.txt", "r")

for tc in range(1, 1+int(input())):
    p, q = map(int, input().split())
    # print(p, q)
    sump = 0

    ii = 0
    for i in range(1, p+1):
        sump += i
        ii = i
        if sump >= p:
            break

    # print('sump', sump)
    a1, b1 = p-(sump-ii), sump-p+1
    # print(a1, b1)

    sumq = 0
    jj = 0
    for j in range(1, q+1):
        sumq += j
        jj = j
        if sumq >= q:
            break

    a2, b2 = q-(sumq-jj), sumq-q+1
    # print(a2, b2)

    a = a1 + a2
    b = b1 + b2
    s = 0
    for n in range(1, a+b):
        s += n

    print('#%d %d' %(tc, s - (a+b-1-a)))






# for tc in range(1, 1+int(input())):
#     p, q = map(int, input().split())
#     print(p, q)
#     arr = [[0]*101 for _ in range(101)]
#     start = 1
#     for i in range(99, -1, -1):
#         arr[i][1] = start
#         for j in range(100-i):
#             arr[i+j][1+j] = start
#             start += 1
#     print(arr)
#
#     final = 10000
#     for j in range(100, 0, -1):
#         arr[0][j] = final
#         for i in range(101-j-1, -1, -1):
#             arr[i][j+i] = final
#             final -= 1
#     print(arr)
#
#     a = 0
#     b = 0
#
#     for i in range(1, 101):
#         for j in range(101):
#             if arr[i][j] == p or arr[i][j] == q:
#                 print('arri f', i, j)
#                 a += i
#                 b += j
#
#     print(a, b)
#     # print(arr[a][b])
#
#     mat = [[0] * 201 for _ in range(201)]
#     start = 1
#     for i in range(199, -1, -1):
#         mat[i][1] = start
#         for j in range(200 - i):
#             mat[i + j][1+j] = start
#             start += 1
#
#     final = 40000
#     for j in range(200, 0, -1):
#         mat[0][j] = final
#         for i in range(201 - j - 1, -1, -1):
#             mat[i][j + i] = final
#             final -= 1
#     print('res', mat[a][b])
