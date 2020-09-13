
def solution(maze):
    answer = 0
    N = len(maze)
    print(maze, answer)
    visited = [[0]*N for i in range(N)]
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    x, y = 0, 0
    flag = True
    while flag:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < N and 0 <= yy < N:
                if not visited[xx][yy]:
                    if maze[xx][yy] == 0:
                        visited[x][y] = 1
                        x = xx
                        y = yy
                        print(x, y)
                        answer += 1
                        if x == N-1 and y == N-1:
                            flag = False
                        break

                        
                elif i > 1:
                    if maze[xx][yy] == 0:
                        visited[x][y] = 1
                        x = xx
                        y = yy
                        print(x, y)
                        answer += 1
                        if x == N-1 and y == N-1:
                            flag = False
                        break

                        
        

    return answer
