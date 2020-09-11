import sys
sys.stdin = open("2819.txt", "r")





dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(i, j):
    stack = [(i, j)]
    visit = []

    while stack:
        for i in range(7):
            y, x = stack.pop(-1)
            visit.append((y, x))

            for n in range(4):
                Y = y + dy[n]
                X = x + dx[n]
                if 0 <= Y < 4 and 0 <= X < 4:
                    # s.append(arr[Y][X])
                    stack.append((Y, X))
        return visit
    #     stack = []
    # return arr





for tc in range(1, 1+int(input())):
    arr = [list(map(int, input().split())) for _ in range(4)]
    print('ori', arr)

    for i in range(4):
        for j in range(4):
            print(dfs(i, j))