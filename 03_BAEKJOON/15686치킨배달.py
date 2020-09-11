import sys
sys.stdin = open('input.txt', 'r')

def comb(k, s):
    global mini
    if k == M:
        sum = 0
        for h in house_pos:
            check = 99999999999999999
            for ch in t:
                if check > abs(h[0]-ch[0]) + abs(h[1]-ch[1]):
                    check = abs(h[0]-ch[0]) + abs(h[1]-ch[1])
            sum += check
        if sum < mini:
            mini = sum

    else:
        for i in range(s, len(chicken_pos) + (k - M) + 1):
            t[k] = chicken_pos[i]
            comb(k+1, i+1)


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken_pos = []
house_pos = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house_pos.append((i, j))
        elif city[i][j] == 2:
            chicken_pos.append((i, j))
# print(house_pos)
# print(chicken_pos)

t = [0]*M
mini = 999999999999999999999999
comb(0, 0)
print(mini)

# 117068 / 204 ms
