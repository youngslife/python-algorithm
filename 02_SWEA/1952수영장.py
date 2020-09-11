import sys
sys.stdin = open('1952.txt', 'r')


def dfs(v, s):
    global mini
    # visited[v] = 1
    if s > mini:
        return
    if v >= 12:
        if s < mini:
            mini = s
        return
    if not plan[v]:
        dfs(v+1, s)
    else:
        # if v+1 <= 12:
            # if not visited[v+1]:
            #     visited[v+1] = 1
        dfs(v+1, s + plan[v]*cost[0])
        dfs(v+1, s + cost[1])
        # if v+3 <= 12:
                # if not visited[v+3]:
                #     visited[v+3] = 1
        dfs(v+3, s + cost[2])






for tc in range(1, 1+int(input())):
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split())) + [0]
    visited = [0]*13
    mini = cost[3]
    dfs(0, 0)
    print('#%d %d' % (tc, mini))

