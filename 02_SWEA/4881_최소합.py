import sys
sys.stdin = open("4881.txt", "r")


def perm_r(k):
    global result
    if k == R:
        total = 0
        for i in range(k):
            total += t[i]
        if total < result:
            result = total


def perm_r(k):
    global result
    if k == R:
        total = 0
        for i in range(k):
            total += t[i]
        if total < result:
            result = total

>>>>>>> e103d0a257b5926870403e567202d4f156b2e708
    else:
        for j in range(N):
            if visited[j]:
                continue
            t[k] = arr[k][j]
            visited[j] = 1
            perm_r(k + 1)
            visited[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    R = N
    t = [0] * R
    visited = [0] * N
    result = 1000000000
    perm_r(0)
    print('#%d %d'%(tc, result))
<<<<<<< HEAD
=======

# def backtrack(a, k, input):
#     global maxcandidates
#     c = [0] * maxcandidates
#
#     if k == input:
#         for r in range(N):
#             for i in range(1, k + 1):
#                 print(a[r][i], end=" ")
#             print()
#     else:
#         k += 1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, input)
#
#
# def construct_candidates(a, k, input, c):
#     in_perm = [False] * NMAX
#
#     for i in range(1, k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#
#     for i in range(1, input + 1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     maxcandidates = N + 1
#     NMAX = N + 1
#     a = [[0] * NMAX for _ in range(N)]
#     backtrack(a, 0, N)
>>>>>>> e103d0a257b5926870403e567202d4f156b2e708


# def backtrack(a, k, input):
#     global maxcandidates
#     c = [0] * maxcandidates
#
#     if k == input:
#         for r in range(N):
#             for i in range(1, k+1):
#                 print(a[][i], end=" ")
#             print()
#     else:
#         k+=1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, input)
#
# def construct_candidates(a, k, input, c):
#     in_perm = [False] * NMAX
#
#     for i in range(1, k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#     for i in range(1, input+1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates
# #
# maxcandidates = 10
# NMAX = 10
# a = [0] * NMAX
# backtrack(a, 0, 3)
#
#
# def backtrack(a, k, input):
#     global maxcandidates
#     c = [0] * maxcandidates
#
#     if k == input:
#         for i in range(1, k+1):
#             print(a[i], end=" ")
#         print()
#     else:
#         k+=1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, input)
#
# def construct_candidates(a, k, input, c):
#     in_perm = [False] * NMAX
#
#     for i in range(1, k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#     for n in range(len(arr)):
#         for m in range(len(arr[n])):
#
#
#     for i in range(1, input+1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates

# 컬럼번호를 가지고 순열을 만든다(row는 항상 일정)

# def backtrack(a, k, input, arr):
#     global maxcandidates
#     global result
#
#     c = [0] * maxcandidates
#
#     if k == input:
#         total = 0
#         for i in range(1, k+1):
#             total += arr[i-1][a[i]-1]  # -1은 0번 인덱스를 버려주기 위해서?
#             if total > result:
#                 break
#         if total < result:
#             result = total
#
#     else:
#         k+=1
#         ncandidates = construct_candidates(a, k, input, c)
#         for i in range(ncandidates):
#             a[k] = c[i]
#             backtrack(a, k, input, arr)
#
# def construct_candidates(a, k, input, c):
#     in_perm = [False] * NMAX
#
#     for i in range(1, k):
#         in_perm[a[i]] = True
#
#     ncandidates = 0
#
#     for i in range(1, input+1):
#         if in_perm[i] == False:
#             c[ncandidates] = i
#             ncandidates += 1
#     return ncandidates
#
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     maxcandidates = N + 1
#     NMAX = N + 1
#     a = [0] * NMAX
#     result = 999
#     backtrack(a, 0, N, arr)
#     print('#%d %d'%(tc, result))
#
#
#     원상복귀시켜주기 위해서 perm값 초기화 (풀이코드)


