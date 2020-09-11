import sys
sys.stdin = open('input1.txt', 'r')

def comb(k, s):
    global mini

    if k == R:
        food2 = list(set(nums)-set(food1))
        synergy1 = 0
        synergy2 = 0
        for i in range(R):
            for j in range(i+1, R):
                synergy1 += S[food1[i]][food1[j]] + S[food1[j]][food1[i]]
                synergy2 += S[food2[i]][food2[j]] + S[food2[j]][food2[i]]
        res = abs(synergy1-synergy2)
        if res < mini:
            mini = res

    else:
        for i in range(s, N + (k-R) + 1):
            food1[k] = i
            comb(k+1, i+1)


for tc in range(1, 1+int(input())):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    nums = [x for x in range(N)]
    R = N // 2
    food1 = [0]*R
    mini = 100000000000000
    comb(0, 0)
    print('#%d %d' % (tc, mini))
