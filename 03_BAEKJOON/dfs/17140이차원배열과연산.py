import sys
sys.stdin = open('input.txt', 'r')

import collections

# 정렬 : 등장 횟수가 커지는 순, 등장 횟수가 같으면 수 가 커지는 순
# 정렬 후 배열 A에 결과를 다시 넣는다.
# 수와 등장 수 모두 넣으며, 순서는 수가 먼저
# 수 정렬시 0은 무시 [3, 2, 0, 0] 정렬 결과 == [3, 2] 정렬 결과

a, b, K = map(int, input().split())
A = [[0]*100 for _ in range(100)]

for i in range(3):
    li = tuple(map(int, input().split()))
    for j in range(len(li)):
        A[i][j] = li[j]
# print(A)

M = 1 # M 1 : 행 >= 열, 2: 행 < 열
# cnts = [0]*101 # 0 ~ 100
# candi = []
result = 0

while A[a-1][b-1] != K:
# for i in range(2):
    y, x = 0, 0  # y는 행, x는 열
    print(A)
    result += 1
    if M == 1:
        f = False

        for i in range(len(A)):
            k = 0
            if A[i][0] == 0:
                if i > y:
                    y = i
                    break
            else:
                cnts = [0] * 101  # 0 ~ 100
                for j in range(len(A[0])):
                    if A[i][j]:
                        cnts[A[i][j]] += 1
                    else:  # A[i][j] == 0 이면 그만
                        break
                # print(cnts)
                # k = 0
                # f = False
                for n in range(1, 101): # 1 ~ 100
                    for c in range(1, len(cnts)): # 1 ~ 100
                        if n == cnts[c]:
                            # print('i', i, c, n)
                            A[i][k] = c
                            A[i][k + 1] = n
                            k += 2
                            if k == 100:
                                # result = -1
                                # A[r-1][k-1] = K
                                # f = True
                                break
                    # if f:
                    # break
                # print('k', k, a-1, b-1)
                # print(A[i][k])
                # print(A[a-1][b-1])
                A[i][k] = 0

                if A[a-1][b-1] > 100:
                    result = -1
                    f = True
                    break
            if k > x:
                x = k
        if f:
            break
        # print(A)
        # print(y, x)
        if y >= x:
            M = 1
        else:
            M = 2
    else:
        f = False
        for j in range(len(A[0])):
            k = 0
            if A[0][j] == 0:  # 문제 점 // 여기서 break 하면 안됨!!!! 그럼 그 다음에 숫자가 있어도 안 세 ㅠ.ㅠ
                if j > x:
                    x = j
            # x == 열
            # print(i)
                    break
            else:
                cnts = [0] * 101 # 0 ~ 100
                for i in range(len(A)):
                    if A[i][j]:
                        cnts[A[i][j]] += 1
                    else:  # A[i][j] == 0 이면 그만
                        if i:
                            break
# print(cnts)
# k = 0
# f = False
                for n in range(1, 101): # 1 ~ 100
                    for c in range(1, len(cnts)): # 1 ~ 100
                        if n == cnts[c]:
                            # print('i', i, c, n)
                            A[k][j] = c
                            A[k+1][j] = n
                            k += 2 # 여기서 k는 행
                            if k == 100:
                                # result = -1
                                # A[r - 1][k - 1] = k
                                # f = True
                                break
                A[k][j] = 0

                if A[a - 1][b - 1] > 100:
                    result = -1
                    f = True
                    break

            if k > y:
                y = k

        if f:
            break

        if y >= x:
            M = 1
        else:
            M = 2

# print(A)
print(result)