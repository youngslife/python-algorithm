import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())
nums = [n for n in range(1, N+1)]

r = -1
L = len(nums)
print('<', end="")
while len(nums) > 1:
     r = (r + K) % len(nums)
     print(nums.pop(r), end=', ')
     r -= 1
     if len(nums) == L % K:
         L = len(nums)
print(nums[0], end='>')

# python3 29212 KB / 56 ms
# pypy3 11759KB / 120 ms
