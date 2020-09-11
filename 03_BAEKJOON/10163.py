import sys
sys.stdin = open("10163.txt", "r")

arr = [[0]*101 for _ in range(101)]

N = int(input())

for n in range(1, N+1):
    info = list(map(int, input().split()))
    p = info[0:2]
    w = info[-2]
    h = info[-1]

    for i in range(p[0], p[0]+w):
        for j in range(p[1], p[1]+h):
             arr[i][j] = n

cnt = [0]*N
for n in range(1, N+1):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == n:
                cnt[n-1] += 1

for i in cnt:
    print(i)


#
# arr = [[0]*101 for _ in range(101)]
#
# N = int(input())
# S = []
# for n in range(1, N+1):
#     info = list(map(int, input().split()))
#     p = info[0:2]
#     w = info[-2]
#     h = info[-1]
#     s = w*h
#     S.append(s)
#     # print(n, p, s, h, w)
#
#     for i in range(p[0], p[0]+w):
#         for j in range(p[1], p[1]+h):
#             if arr[i][j] == 0:
#                 arr[i][j] = n
#             else:
#                 for k in range(1, n):
#                     if arr[i][j] == n-k:
#                         S[n-k-1] -= 1
#                 arr[i][j] = n
# for i in S:
#     print(i)



# for _ in range(4):
#     rec = list(map(int, input().split()))
#
#     for n in range(rec[0], rec[2]):
#         for m in range(rec[1], rec[3]):
#             arr[n][m] = 1
#
# cnt = 0
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] == 1:
#             cnt += 1
#
# print(cnt)