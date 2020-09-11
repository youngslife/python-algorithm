import sys
sys.stdin = open('input.txt', 'r')
# sys.setrecursionlimit(100000)
# import collections

def dfs(N, t):
    global K, mini
    if t > mini:
        return
    if N == K:
        if t < mini:
            mini = t
            return
    elif N < K:
        if 2 <= N * 2 <= 100000:
            dfs(N*2, t+1)
        if 0 <= N + 1 <= 100000:
            dfs(N+1, t+1)
        if 0 <= N - 1 < 100000:
            dfs(N-1, t+1)
    else:
        if 0 <= N - 1 < 100000:
            dfs(N-1, t+1)

# def dfs(N):
#     global K, t
#     visited = [0]*100001
#     s = [N]
#     visited[N] = 1
#     while s:
#         n = s.pop(-1)
#         if n == K:
#             return t
#         else:
#             if n > K:
#                 if not visited[n-1]:
#                     visited[n-1] = 1
#                     s.append(n-1)
#             if n < K:
#                 if 0<=n-1<100001 and not visited[n-1]:
#                     visited[n-1] = 1
#                     s.append(n-1)
#                 if 0<=n+1<100001 and not visited[n+1]:
#                     visited[n+1] = 1
#                     s.append(n+1)
#                 if 0<=n*2<100001 and not visited[n*2]:
#                     visited[n*2] = 1
#                     s.append(n*2)
#         t += 1
N, K = map(int, input().split())
mini = abs(K - N)
dfs(N, 0)
# print(t)

print(mini)


#
# TEST CASE #3:
# 15964 89498
# exp -> 4781
# you -> 19110
