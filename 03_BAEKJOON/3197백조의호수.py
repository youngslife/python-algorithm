import sys
sys.stdin = open("input.txt", "r")


def bfs(swan):
    q = [(swan[0], swan[1])]
    visited = [[0]*C for _ in range(R)]
    visited[swan[0]][swan[1]] = 1

    while q:
        y, x = q.pop(0)
        for dy, dx in (0, 1), (1, 0), (0, -1), (-1, 0):
            if 0 <= y + dy < R and 0 <= x + dx < C and not visited[y+dy][x+dx]:
                if lake[y+dy][x+dx] == 'L':
                    return True
                elif lake[y+dy][x+dx] == '.':
                    q.append((y+dy, x+dx))
                    visited[y+dy][x+dx] = 1
    return False


R, C = map(int, input().split())
lake = [list(input()) for _ in range(R)]
meet = False
day = 0
ice = 0
swan = []
for r in range(R):
    for c in range(C):
        if lake[r][c] == 'L':
            swan.append((r, c))
        elif lake[r][c] == 'X':
            ice += 1


while not meet:
    if bfs(swan[0]):
        meet = True
    else:
        day += 1
        checked = [[0] * C for _ in range(R)]
        for y in range(R):
            for x in range(C):
                if lake[y][x] == '.' and not checked[y][x]:
                    checked[y][x] = 1
                    for dy, dx in (0, 1), (1, 0), (0, -1), (-1, 0):
                        if 0 <= y + dy < R and 0 <= x + dx < C and not checked[y + dy][x + dx]:
                            checked[y + dy][x + dx] = 1
                            if lake[y + dy][x + dx] == 'X':
                                lake[y + dy][x + dx] = '.'
                                ice -= 1



print(day)

