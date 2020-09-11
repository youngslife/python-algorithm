import sys
sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

visited = [[0]*N for _ in range(N)]
for i in range(N):
    # std = arr[i][0]
    # stdL = 1
    sL = 1
    visited[i][0] = 1
    flag = False
    for j in range(1, N):
        if not visited[i][j]:
            if arr[i][j] - arr[i][j-1] == 0:
                sL += 1
                visited[i][j] = 1

            elif arr[i][j] - arr[i][j-1] == 1:
                if sL >= L:
                    sL = 1
                    visited[i][j] = 1
                    continue
                else:
                    break
            elif arr[i][j] - arr[i][j-1] == -1:
                if j + L - 1 < N:
                    for n in range(1, L):
                        if arr[i][j+n] == arr[i][j]:
                            continue
                        else:
                            flag = True
                            break
                    else:
                        for k in range(L):
                            visited[i][j+k] = 1
                        sL = 0
                else:
                    break
            else:
                break
        if flag:
            break
    else:
        # print(i)
        cnt += 1
# print(cnt)
# print('--------------')

visited = [[0]*N for _ in range(N)]
for j in range(N):
    sL = 1
    visited[0][j] = 1
    flag = False
    for i in range(1, N):
        if not visited[i][j]:
            if arr[i][j] - arr[i-1][j] == 0:
                sL += 1
                visited[i][j] = 1

            elif arr[i][j] - arr[i-1][j] == 1:
                if sL >= L:
                    sL = 1
                    visited[i][j] = 1
                    continue
                else:
                    break
            elif arr[i][j] - arr[i-1][j] == -1:
                if i + L - 1 < N:
                    for n in range(1, L):
                        if arr[i+n][j] == arr[i][j]:
                            continue
                        else:
                            flag = True
                            break
                    else:
                        for k in range(L):
                            visited[i+k][j] = 1
                        sL = 0
                else:
                    break
            else:
                break
        if flag:
            break
    else:
        # print(j)
        cnt += 1
print(cnt)

# 115440 KB / 144ms





