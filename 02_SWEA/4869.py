import sys
sys.stdin = open("4869.txt", "r")


# def f(N):
#     if N == 1:
#         return 1
#     if N == 2:
#         return 3
#     if N in range(3, 31):
#         return f(N-1) + 2 * f(N-2)
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) // 10
#     print("#%d %d" % (tc, f(N)))




def attach(N):
    if N == 1:
        return 1
    if N == 2:
        return 3
    if N in range(3, 31):
        return attach(N-1) + 2 * attach(N-2)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10
    print("#%d %d" % (tc, attach(N)))


