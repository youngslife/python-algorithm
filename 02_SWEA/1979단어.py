import sys
sys.stdin = open("1979.txt", "r")

def isWall(i, j):
    if i < 0 or i>=N or j < 0 or j >= N:
        return True
    return False

def func(arr, i, j):
    if isWall(i, j-1) or arr[i][j-1] == 0:
        for n in range(j, j+K):
            if arr[i][n] == 1:
                continue
            else:
                return False
        if isWall(i, j+K) or arr[i][j+K] == 0:
            return True
    return False
    # return True
    # if arr[i][j+K] == 0:
    #     cnt += 1
    #     for n in range(j, j+K):
    #         arr[i][n] = 0
    # return
def func2(arr, i, j):
    if isWall(i-1, j) or arr[i-1][j] == 0:
        for n in range(i, i+K):
            if arr[n][j] == 1:
                continue
            else:
                return False
        if isWall(i+K, j) or arr[i+K][j] == 0:
            return True
    return False
# def func2(arr, i, j):
#     global cnt
#     if arr[i+K][j] == 0:
#         cnt += 1

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N-K+1):
            if arr[i][j] == 1:
                # print('ij', i, j)
                if func(arr, i, j):
                    # print(arr, i, j)
                    cnt += 1
    for j in range(N):
        for i in range(N-K+1):
            if arr[i][j] == 1:
                if func2(arr,i,j):
                    cnt += 1

    print('#%d %d'%(tc, cnt))




