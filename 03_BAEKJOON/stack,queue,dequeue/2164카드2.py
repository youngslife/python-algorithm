import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
nums = [n for n in range(1, N+1)]
n = 0
while len(nums) > 1:
    for i in range(len(nums)-1, -1, -1):
        if i % 2 == 0:
            nums.pop(i)

print(nums[0])

# deque 이용
import collections

N = int(input())
nums = collections.deque(n for n in range(1, N+1))

while len(nums) > 1:
    nums.popleft()
    nums.append(nums.popleft())

print(nums[0])



# 시간 초과 코드
import collections

N = int(input())
nums = collections.deque(n for n in range(1, N+1))

while len(nums) > 1:
    for i in range(len(nums)-1, -1, -1):
        if i % 2 == 0:
            nums.remove(nums[i])

print(nums[0])
