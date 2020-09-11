import sys
sys.stdin = open('input.txt', 'r')

def divide(arr, s1, s2, N):  # s1: 행의 시작 범위, s2: 열의 시작 범위, N 행렬의 크기
    check = arr[s1][s2]  # 행렬의 첫번째 값
    flag = False  # for문 멈추기 위해 설정
    for i in range(s1, s1+N):
        for j in range(s2, s2+N):
            if arr[i][j] != check:  # check와 다른 값 나오면 4개라 분할한 후 재귀
                print('(', end="")
                divide(arr, s1, s2, N//2)
                divide(arr, s1, s2+N//2, N//2)
                divide(arr, s1+N//2, s2, N//2)
                divide(arr, s1+N//2, s2+N//2, N//2)
                print(')', end="")
                flag = True
                break
        if flag:
            break
    else:                 # for문이 무사히 끝나면 그 값을 출력
        if check == '0':  # arr를 받을 때 int로 안받고 바로 list(input())으로 받아서 str으로 확인
            print(0, end="")
        else:
            print(1, end="")



N = int(input())  # 1<=N<=64 (영상의 크기)
arr = [list(input()) for _ in range(N)]

divide(arr, 0, 0, N)

# 121328 KB / 232 ms
