import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

n = int(input())
answer = [int(input()) for _ in range(n)]
idx = 0
stack = deque([])
res = ''
popcnt = 0
for i in range(1, n+1):
    stack.append(i)
    res += '+'
    if stack[-1] == answer[idx]:
        stack.pop()
        popcnt += 1
        res += '-'
        idx += 1
        for j in range(len(stack)-1, -1, -1):
            if stack[j] == answer[idx]:
                stack.pop()
                popcnt += 1
                res += '-'
                idx += 1
            else:
                break
if popcnt == n:
    for s in res:
        print(s)
else:
    print('NO')

# python3 일 때 35776 KB / 4176 ms
# pypy3 일 때 실패