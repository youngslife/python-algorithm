import sys
sys.stdin = open("input4861.txt", "r")
# M 길이 만큼의 문자열 동안 앞뒤가 같은걸 찾아야해
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        # arr += input().split()
        arr.append(input())  # 이차원 배열


    for i in range(len(arr)):
        for j in range(N):
            origin = arr[i][j:j+M]  # 전체 텍스트
        # origin = arr[i]
            rev = origin[::-1]  # 찾을 패턴

            # print(origin, rev)
            # Brute Force방법을 리스트에서 사용
            p = 0  # rev의 인덱스
            t = 0  # origin 인덱스
            if len(origin) == M:
                while p < len(rev) and t < len(origin):
                    if origin[t] != rev[p]:
                        t = t - p
                        p = -1
                    t = t + 1
                    p = p + 1
                if p == len(rev):
                    print('#{} {}'.format(tc, origin))




    c = []
    col = []
    for j in range(len(arr[0])):
        for i in range(len(arr)):
            c.append(arr[i][j])
        col.append(c)
        c = []

    for k in range(len(col)):
        for j in range(N):
            ori = col[k][j:j + M]
            re = ori[::-1]

            p = 0
            t = 0

            if len(ori) == M:
                while p < len(re) and t < len(ori):
                    if ori[t] != re[p]:
                        t = t - p
                        p = -1
                    t = t + 1
                    p = p + 1
                if p == len(re):
                    print('#{}'.format(tc), end=" ")
                    res = ''
                    for m in ori:
                        res += m
                    print(res)
