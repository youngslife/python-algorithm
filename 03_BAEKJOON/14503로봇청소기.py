import sys
sys.stdin = open("input.txt", "r")
# 115436KB / 144ms
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dy = [-1, 0, 1, 0]  # 북 동 남 서
dx = [0, 1, 0, -1]

ing = False
res = 0

def two():
    global r, c, d
    turn = 0
    for _ in range(4):

        d = (d + 3) % 4
        y = r + dy[d]
        x = c + dx[d]
        if not arr[y][x] and not visited[y][x]:
            r, c = y, x
            return turn  # 다시 1번으로
        turn += 1
    return turn


while not ing:
    # 현재 위치 청소
    if not arr[r][c] and not visited[r][c]:
        visited[r][c] = 1
        res += 1
    # 2번
    f = False
    while not f:
        check = two()

        if check < 4:
            break
        else:
            back = (d+2) % 4
            by = r + dy[back]
            bx = c + dx[back]
            if 0 <= by < N or 0 <= bx < M:
                if arr[by][bx]:
                    ing = True
                    break
                r, c = by, bx  # 한칸 후진
            else:
                ing = True
                break

print(res)
