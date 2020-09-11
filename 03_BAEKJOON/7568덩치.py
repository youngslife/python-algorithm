import sys
sys.stdin = open("input.txt", "r")

N = int(input())  # 전체 사람의 수
li = []
res = [0]*N
for _ in range(N):
    li.append(tuple(map(int, input().split())))

for i in range(N):
    idx = 1
    w, h = li[i]
    for j in range(N):
        if i == j:
            continue
        if w < li[j][0] and h < li[j][1]:
            idx += 1
    res[i] = idx

for i in res:
    print(i, end=" ")


