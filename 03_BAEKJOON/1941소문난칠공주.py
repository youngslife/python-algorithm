import sys
sys.stdin = open("input.txt", "r")


def dfs(i, j, temp):  # 자리 판단
    visited = [[0] * 5 for _ in range(5)]
    s = [(i, j)]
    # print('s', s)
    check = []
    while s:
        y, x = s.pop(-1)
        if not visited[y][x]:
            visited[y][x] = 1
            check.append((y, x))
            # print(check)
            for dy, dx in (1, 0), (-1, 0), (0, 1), (0, -1):
                Y = y + dy
                X = x + dx
                # print(Y, X)
                if not (0 <= X < 5 and 0 <= Y < 5):
                    continue
                if (Y, X) in temp:
                    # print('temp check', Y, X)
                    if not visited[Y][X]:
                        s.append((Y, X))
    if len(check) == 7:
        return True
    else:
        return False


def comb(k, s):  # 7 명 조합
    global cnt
    if k == 7:
        # print(t)
        sCnt = 0

        for i, j in t:
            if sit[i][j] == 'S':
                sCnt += 1
        if sCnt >= 4:
            if dfs(t[0][0], t[0][1], t):
                cnt += 1
    else:
        for i in range(s, 25 + (k - 7)+ 1):
            t[k] = people[i]
            comb(k+1, i+1)


sit = [list(input()) for _ in range(5)]  # 교실 자리

people = [(a, b) for a in range(5) for b in range(5)]  # 25명 조합을 위한 list

t = [0]*7
cnt = 0
comb(0, 0)
print(cnt)

