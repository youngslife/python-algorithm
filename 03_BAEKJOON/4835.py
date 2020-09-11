import sys
sys.stdin = open("input4.txt", "r")

def segment(N, M, nums):
    maxValue = sum(nums[:M])
    minValue = sum(nums[:M])
    for i in range(N-M+1):
        if sum(nums[i:i+M]) > maxValue:
            maxValue = sum(nums[i:i+M])
        if sum(nums[i:i+M]) < minValue:
            minValue = sum(nums[i:i+M])
    return maxValue - minValue



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    result = segment(N, M, nums)
    print('#%d %d' % (tc, result))