import sys
sys.stdin = open('5205.txt', 'r')


def partition(li, p, r):
    x = li[r]
    i = p - 1
    for j in range(p, r):
        if li[j] <= x:
            i += 1
            li[i], li[j] = li[j], li[i]
    li[i+1], li[r] = li[r], li[i+1]
    return i + 1


def sort(li, p, r):
    if p < r:
        s = partition(li, p, r)
        if s == N // 2:
            return
        else:
            sort(li, p, s-1)
            sort(li, s+1, r)
    return

for tc in range(1, 1+int(input())):
    N = int(input())
    nums = list(map(int, input().split()))

    sort(nums, 0, len(nums)-1)
    print('#%d %d' % (tc, nums[N // 2]))


