import sys
sys.stdin = open('5208.txt', 'r')


def solve(stop, n):
    global res
    # print('1', Ms[stop-1])
    if n > res:
        return

    else:
        for s in range(Ms[stop-1], 0, -1):
            if stop + s < N:
                solve(stop+s, n+1)
            else:
                if res > n:
                    res = n
                    return

for tc in range(1, 1+int(input())):
    info = list(map(int, input().split()))
    N = info[0]
    Ms = info[1:]

    res = N
    solve(1, 0)
    print('#%d %d'%(tc, res))




# def powerset(k, total):
#     global ans
#
#     if k == N - 2:
#         # print(a, total)
#         n = 0  # 부분집합 크기
#
#         s = 1
#         for i in range(len(a)):
#             if a[i] == 1:
#                 n += 1
#
#                 if N > s + Ms[s-1] >= i + 2:
#                     s = i+2
#                 elif s + Ms[s-1] >= N:
#                     # print('iniininin')
#                     if ans > n:
#                         ans = n
#                     break
#                 else:
#                     break
#         else:
#             if s + Ms[s-1] >= N:
#                 if ans > n:
#                     ans = n
#
#     else:
#         a[k] = 1
#         powerset(k+1, k + Ms[k+1])
#         a[k] = 0
#         powerset(k+1, k + Ms[k+1])

