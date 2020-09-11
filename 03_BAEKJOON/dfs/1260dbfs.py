import sys
sys.stdin = open('input.txt', 'r')


# def dfs(v):
#     stack = [v]
#     print(stack.pop(-1), end=" ")
#     visited[v] = 1
#     for i in range(len(arr[v])):
#         if arr[v][i] and not visited[i]:
#             stack.append(i)
#             arr[v][i] = 0
#             dfs(i)


def bfs(v):
    q = [v]
    visited[v] = 1
    print(v, end=" ")
    while q:
        p = q.pop(0)
        for i in range(len(arr[p])):
            if arr[p][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
                print(i, end=" ")


N, M, V = map(int, input().split())
arr = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

dfs(V)
print()
visited = [0]*(N+1)
bfs(V)
