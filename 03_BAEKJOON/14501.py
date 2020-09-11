import sys
sys.stdin = open("bj14501.txt", "r")

def solve(k, sum):
    if k == N-1:
        if sum == N:
            for i in range(N):
                if a[i] == True:
                    print(Ts[i], end=' ')
            print()
        if sum > 7:
            return
    else:
        k += 1
        if sum + Ts[k] <= N:
            a[k] = 1; solve(k, sum + Ts[k])

        # a[k] = 1; backtrack(k, sum + k)
        a[k] = 0; solve(k, sum)

# N = 10
# a = [0] * (N + 1)
#
# cnt = 0
# solve(0, 0)
# print("cnt : ", cnt)


for tc in range(1, 1+int(input())):
    N = int(input())
    Ts = []
    Ps = []
    for i in range(N):
        T, P = map(int, input().split())
        Ts.append(T)
        Ps.append(P)

    print(Ts, Ps)

    a = [0] * (N+1)
    solve(-1, 0)