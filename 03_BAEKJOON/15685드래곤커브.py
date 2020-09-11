import sys
sys.stdin = open('input.txt', 'r')
     # 우, 상, 좌, 하
     # 0, 1, 2, 3
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
N = int(input())
arr = [[0]*101 for _ in range(101)]
# 그 곳에 가면 visited처리 하기
for _ in range(N):
    x, y, d, g = map(int, input().split())
    arr[y][x] = 1
    dirs = [d]
    a, b = x, y
    for _ in range(g+1):
        x, y = a, b
        print(dirs)
        for n in range(len(dirs)-1, -1, -1):
            Y = y + dy[dirs[n]]
            X = x + dx[dirs[n]]
            # if 0 <= Y < 100 and 0 <= X < 100:
            arr[Y][X] = 1
            x, y = X, Y
            print('arr', (Y, X))
            if dirs[n] < 3:
                d = dirs[n] + 1
                dirs.append(d)
            elif dirs[n] == 3:
                d = 0
                dirs.append(d+1)
cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            for y, x in (0, 1), (1, 0), (1, 1):
                if arr[i+y][j+x] == 1:
                    continue
                else:
                    break
            else:
                cnt += 1
print(cnt)




