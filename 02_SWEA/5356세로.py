import sys
sys.stdin = open("5356.txt", "r")

# T = int(input())
# for tc in range(1, T+1):
#     arr = [[None]*15 for _ in range(5)]
#     # print(arr)
#     for i in range(5):
#         put = input()
#         for j in range(len(put)):
#             arr[i][j] = put[j]
#     # print(arr)
#
#     result = ''
#
#     for j in range(15):
#         for i in range(5):
#             if arr[i][j] == None:
#                 continue
#             else:
#                 result += arr[i][j]
#     print('#%d %s' % (tc, result))

T = int(input())
for tc in range(1, T + 1):
    board = [list(input()) for _ in range(5)]
    print(board)

    result = ''
    for c in range(15):
        for r in range(5):
            try:
                result += board[r][c]
            except IndexError:
                pass
    print('#%d %s' % (tc, result))

