import sys
sys.stdin = open('input3.txt', 'r')

for tc in range(1, 1+int(input())):
    N = int(input())  # 학생 수
    M = int(input())  # 비교 횟수
    arr = [[0]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
    # print(arr)

    nums = [0]*(N+1)
    # print(nums)

    for i in range(N+1):
        visited = [0] * (N + 1)
        q = []
        for j in range(N+1):
            if arr[i][j]:
                nums[i] += 1
                visited[j] = 1
                q.append(j)

        while q:
            for _ in range(len(q)):
                n = q.pop(0)
                # print(n)
                for k in range(N+1):
                    if arr[n][k]:
                        if not visited[k]:
                            visited[k] = 1
                            nums[i] += 1
                            q.append(k)
    print(nums)
    for j in range(N+1):
        visited = [0] * (N + 1)
        q = []
        for i in range(N+1):
            # q = []
            if arr[i][j]:
                nums[j] += 1
                visited[i] = 1
                q.append(i)
        while q:
            for _ in range(len(q)):
                n = q.pop(0)
                for k in range(N+1):
                    if arr[k][n]:
                        if not visited[k]:
                            visited[k] = 1
                            nums[j] += 1
                            q.append(k)
    print(nums)


    cnt = 0
    for n in nums:
        if n == N-1:
            cnt += 1

    print('#%d %d' % (tc, cnt))

