import sys
sys.stdin = open("2669.txt", "r")


# arr = [[0]*101 for _ in range(101)]
#
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

arr = [[0]*9 for _ in range(9)]

for _ in range(4):
    rec = list(map(int, input().split()))

    for n in range(rec[0], rec[2]):
        for m in range(rec[1], rec[3]):
            arr[-1-n][-1-m] = 1
    print(arr)

cnt = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)