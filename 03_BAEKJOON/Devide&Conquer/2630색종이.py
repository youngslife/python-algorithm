import sys
sys.stdin = open('input.txt', 'r')


def check(paper, s1, s2, N):  # s1: i(행)의 시작 범위, s2: j(열)의 시작 범위, N: 범위 길이
    global cntB, cntW
    color = paper[s1][s2]  # 주어진 범위의 정사각형의 첫번째 칸 색
    flag = False  # for문 2개를 멈추기 위한 flag
    for i in range(s1, s1+N):
        for j in range(s2, s2+N):
            if paper[i][j] != color:  # 첫번째 칸과 색이 다를때 재귀
                check(paper, s1, s2, N//2)  # 왼쪽 위
                check(paper, s1+N//2, s2, N//2)  # 왼쪽 아래
                check(paper, s1, s2+N//2, N//2)  # 오른쪽 위
                check(paper, s1+N//2, s2+N//2, N//2)  # 오른쪽 아래
                flag = True
                break
        if flag:
            break
    else:  # for-else문으로, for문의 범위 내 모두 색깔이 같으면 cnt +
        if color == 0:
            cntW += 1
        else:
            cntB += 1



N = int(input())  # 주어진 색종이의 한변의 길이(2, 4, 8, ..., 128)
paper = [list(map(int, input().split())) for _ in range(N)]  # 0: 흰색, 1: 파란색
cntW = 0  # 흰색 카운트
cntB = 0  # 파란색 카운트

check(paper, 0, 0, N)
print(cntW)
print(cntB)

# 116079 KB / 164 ms