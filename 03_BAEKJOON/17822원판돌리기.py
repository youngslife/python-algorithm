import sys
sys.stdin = open('input.txt', 'r')
# di: 0, 시계 방향; 1, 반시계

N, M, T = map(int, input().split())
# adj = False
nums = [[] for i in range(N)]

for i in range(N):
    nums[i] = list(map(int, input().split()))
# print(nums)


for t in range(T):
    x, d, k = map(int, input().split())
    # print(x, d, k)
    adj = False
    for i in range(N):
        if (i+1) % x == 0:
            if d:  # 반시계
                temp = [0]*M
                for n in range(M):
                    temp[(n-k)%M] = nums[i][n]
                nums[i] = temp
            else:  # 시계
                temp = [0] * M
                for n in range(M):
                    temp[(n + k) % M] = nums[i][n]
                nums[i] = temp

    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if nums[i][j]:
                c = nums[i][j]
                if nums[i][(j-1) % M] == c:
                    adj = True
                    visited[i][j] = 1
                    visited[i][(j-1) % M] = 1
                if nums[i][(j+1) % M] == c:
                    adj = True
                    visited[i][j] = 1
                    visited[i][(j+1) % M] = 1
                if 0 <= i - 1 < N:
                    if nums[i-1][j] == c:
                        adj = True
                        visited[i][j] = 1
                        visited[i-1][j] = 1
                if 0 <= i + 1 < N:
                    if nums[i+1][j] == c:
                        adj = True
                        visited[i][j] = 1
                        visited[i+1][j] = 1
    if adj:
        for i in range(N):
            for j in range(M):
                if visited[i][j]:
                    nums[i][j] = 0
    else:
        cnt = 0
        s = 0
        for i in range(N):
            for j in range(M):
                if nums[i][j]:
                    s += nums[i][j]
                    cnt += 1
        if not cnt:
            break
        avg = s / cnt
        # print('avg', s, cnt, avg)
        for i in range(N):
            for j in range(M):
                if nums[i][j]:
                    if nums[i][j] < avg:
                        nums[i][j] += 1
                    elif nums[i][j] > avg:
                        nums[i][j] -= 1
    # print('change', nums)
print(sum(sum(nums, [])))





