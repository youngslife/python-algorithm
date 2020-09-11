import sys
sys.stdin = open("input.txt", "r")

N = int(input())  # 시험장 수
A = list(map(int, input().split()))  # 각 시험장 응시자 수
B, C = map(int, input().split())  # 총감 감시자수, 부감 감시자수
ans = 0
for a in A:
    if a < B:
        continue
    else:
        if (a - B) % C == 0:
            ans += (a-B) // C
        else:
            ans += (a-B) // C + 1

print(ans + N)