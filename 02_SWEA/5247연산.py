import sys
sys.stdin = open('5247.txt', 'r')

from collections import deque


for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    cnt = 0
    q = deque([N])
    found = False
    visited = [0] * 1000001
    while q:
        cnt += 1
        for i in range(len(q)):
            t = q.popleft()
            li = [t+1, t-1, t*2, t-10]
            for i in li:
                if i > 10**6 or i < 1:
                    continue
                elif i == M:
                    found = True
                    break
                else:
                    if not visited[i]:
                        q.append(i)
                        visited[i] = True
        if found:
            break


    print('#%d %d' % (tc, cnt))
    print(time.time()-s)

# 뒤에서부터 연산
# 홀수일때 더하기 빼기, 짝수일때 나누기 연산



# 갔던 곳을 또 가도 됨.
# 탐색 시 visited체크 할 필요없이 답 찾을때까지
# dfs/ bfs 로 처리할 수 있음