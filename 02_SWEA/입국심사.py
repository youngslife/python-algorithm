import sys
sys.stdin = open('input.txt', 'r')

def binary():
    low = 0
    high = 10**18

    while low < high:
        mid = (low + high) // 2
        n = 0
        for t in time:
            n += mid // t
        if n < M:
            low = mid + 1
        else:
            high = mid
    return low

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    time = [int(input()) for _ in range(N)]

    print('#%d %d' % (tc, binary()))

# T = int(input())
# for tc in range(T):
#     n, m = map(int, input().split())
#     data = list(int(input()) for _ in range(n))
#     min_t = min(data)
#     left = 0
#     right = min_t * m
#     while left < right:
#         mid = (right + left) // 2
#         finished = sum([mid // d for d in data])
#         if finished < m:
#             left = mid + 1
#         else:
#             right = mid
#     print("#{} {}".format(tc + 1, left))