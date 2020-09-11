import sys
sys.stdin = open('input.txt', 'r')


def perm(k, turn):
    global ans
    if k == 8:
        for t in range(turn):
            s = score[t]
            temp = [0, 0, 0, 0]
            out = 0
            while out < 3:
                for n in range(3):
                    if s[n] > 0:
                        temp[s[n]-1] += 1

                    else:
                        out += 1

            print()
    else:
        for i in range(k, 8):
            nums[k], nums[i] = nums[i], nums[k]
            perm(k+1)
            nums[k], nums[i] = nums[i], nums[k]


N = int(input())
nums = [n for n in range(1, 9)]
score = [[] for _ in range(N)]
for n in range(N):
    s = list(map(int, input().split()))
    score[n] = s



ans = 0
perm(0, 1)





