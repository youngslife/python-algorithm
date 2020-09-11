import sys
sys.stdin = open('2115.txt', 'r')


+


# 1번째 풀이(오답 2개)
# def comb(k, s):
#     global maxi
#     if k == 2:
#         print(t)
#         for l in t[0]:
#             if l in t[1]:
#                 return
#         else:  # 문제점: 각 값들의 부분집합을 구하고, 부분집합의 v**2합이 최대일때 res / sort 과정을 필요 없음.
#             res = 0
#             for i in range(2):
#                 n = 0
#                 t[i].sort(key=lambda x: x[-1], reverse=True)
#                 for j in range(len(t[i])):
#                     a, b, v = t[i][j]
#                     if n + v <= C:
#                         n += v
#                         res += v**2
#                     else:
#                         break
#             if res > maxi:
#                 maxi = res
#             print(res)
#
#     else:
#         for i in range(s, len(candi) + (k-2) + 1):
#             t[k] = candi[i]
#             comb(k+1, i+1)

