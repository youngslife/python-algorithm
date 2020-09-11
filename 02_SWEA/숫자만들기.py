import sys
sys.stdin = open('input1.txt', 'r')

def dfs(v, sum, p, m, g, d):
    global mini, maxi
    # print(sum)

    if v == N-1:
        if sum < mini:
            mini = sum
        if sum > maxi:
            maxi = sum
        return
    if p:
        dfs(v+1, sum + nums[v+1], p-1, m, g, d)
    if m:
        dfs(v+1, sum - nums[v+1], p, m-1, g, d)
    if g:
        dfs(v + 1, sum * nums[v + 1], p, m, g-1, d)
    if d:
        if sum < 0:
            temp = -(abs(sum) // nums[v+1])
        else:
            temp = sum // nums[v+1]
        dfs(v + 1, temp, p, m, g, d-1)



for tc in range(1, 1+int(input())):
    N = int(input())
    p, m, g, d= map(int, input().split())
    nums = list(map(int, input().split()))
    visited = [0]*N
    # print(p, m, g, d)
    # print(nums)

    # li = ['+']*onum[0] + ['-']*onum[1] + ['*']*onum[2] + ['/']*onum[3]

    mini = 10000000000
    maxi = -10000000000

    dfs(0, nums[0], p, m, g, d)
    print('#%d %d' % (tc, maxi-mini))