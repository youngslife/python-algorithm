import sys
sys.stdin = open('input.txt', 'r')

a, b, K = map(int, input().split())
A = [[0]*100 for _ in range(100)]

for i in range(3):
    li = tuple(map(int, input().split()))
    for j in range(len(li)):
        A[i][j] = li[j]
# print(A)

M = 1 # M 1 : 행 >= 열, 2: 행 < 열
result = 0

while A[a-1][b-1] != K:
    y, x = 0, 0  # y는 행, x는 열
    print(A)
    result += 1
    if M == 1:
        f = False
          # 행 개수
        for i in range(len(A)):
            k = 0
            cnts = [0] * 101  # 0 ~ 100
            for j in range(len(A[0])):
                if A[i][j]:
                    cnts[A[i][j]] += 1
                else:  # A[i][j] == 0 이면 그만
                    if i:
                        break

            flag = False
            ### 여기서 돌면서 먼저 A[i][j]를 0으로 reset 해보자!!!! 어차피 다 도니까는,,,
            for n in range(1, 101): # 1 ~ 100
                for c in range(1, len(cnts)): # 1 ~ 100
                    if n == cnts[c]:
                        A[i][k] = c
                        A[i][k + 1] = n
                        k += 2
                        if k == 100:
                            flag = True
                            break
                if flag:
                    break

                for z in range(k, 100):   #
                    A[i][z] = 0
            if k > x:
                x = k
        if A[a-1][b-1] > 100:
            result = -1
            f = True
            break

        for nn in range(100):
            if A[nn][0]:
                y += 1
            else:
                break
        print('R', A)
        print('M=1, y, x', y, x)
        if y >= x:
            M = 1
        else:
            M = 2
        if f:
            break
    else:
        f = False

        for j in range(len(A[0])):

            k = 0
            # if A[0][j] == 0:  # 문제 점 // 여기서 break 하면 안됨!!!! 그럼 그 다음에 숫자가 있어도 안 세 ㅠ.ㅠ

            cnts = [0] * 101 # 0 ~ 100
            for i in range(len(A)):
                if A[i][j]:
                    cnts[A[i][j]] += 1
                else:  # A[i][j] == 0 이면 그만
                    if i:
                        break

            flag = False
            for n in range(1, 101): # 1 ~ 100
                for c in range(1, len(cnts)): # 1 ~ 100
                    if n == cnts[c]:
                        # print('i', i, c, n)
                        A[k][j] = c
                        A[k+1][j] = n
                        k += 2 # 여기서 k는 행
                        if k == 100:

                            flag = True
                            break
                if flag:
                    break

                for z in range(k, 100):
                    A[z][j] = 0

            if k > y:
                y = k
        # print('want', A[a - 1][b - 1])
        if A[a - 1][b - 1] > 100:
            result = -1
            f = True
            break

        for nn in range(100):
            if A[0][nn]:
                x += 1
            else:
                break

        print('R', A)
        print('M=2, y, x', y, x)
        if y >= x:
            M = 1
        else:
            M = 2
        if f:
            break

# print(A)
print(result)