import collections

N, M = map(int, input().split())
goal = collections.deque(map(int, input().split()))

q = collections.deque([n for n in range(1, 1+N)])
mid = (len(q)-1) // 2
cnt = 0
for n in goal:
    if n == q[0]:
        q.popleft()
    elif q.index(n) <= mid:
        while q[0] != n:
            cnt += 1
            q.append(q.popleft())
        q.popleft()
    elif q.index(n) > mid:
        while q[0] != n:
            cnt += 1
            q.appendleft(q.pop())
        q.popleft()
    if q:
        mid = (len(q)-1)//2

print(cnt)
