import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
li = [[] for _ in range(N+1)]  # 인접리스트
inDegree = [0 for _ in range(N+1)]

# input값으로 인접리스트 만들기
for i in range(M):
    temp = list(map(int, input().split()))
    for j in range(temp[0]-1):
        li[temp[j+1]] += [temp[j+2]]

# 인접리스트로 inDgree list 만들기
for n in range(1, N+1):
    if li[n]:
        for i in li[n]:
            inDegree[i] += 1

# topological sort
q = []
res = []
isCycle = False

for i in range(1, len(inDegree)):
    if inDegree[i] == 0:
        q.append(i)
# 0인 indegree가 없을 때

if not q:
    q.append(inDegree[0])

for _ in range(N):
    if not q:
        isCycle = True
        break

    v = q.pop(0)
    res.append(v)

    for u in li[v]:
        inDegree[u] -= 1
        if inDegree[u] == 0:
            q.append(u)
if isCycle:
    print(0)
else:
    for r in res:
        print(r)

