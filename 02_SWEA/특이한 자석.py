import sys
sys.stdin = open('input2.txt', 'r')


for tc in range(1, 1+int(input())):
    K = int(input())
    m1 = list(map(int, input().split()))
    m2 = list(map(int, input().split()))
    m3 = list(map(int, input().split()))
    m4 = list(map(int, input().split()))
    f = [0, 0, 0, 0, 0]

    for _ in range(K):
        num, d = map(int, input().split())
        d = -d
        interface = [1]*3

        ## f를 기준으로 다시 하기
        for _ in range(3):
            if m1[(f[1]+2)%8] == m2[(f[2]+6)%8]:
                interface[0] = 0
            if m2[(f[2]+2)%8] == m3[(f[3]+6)%8]:
                interface[1] = 0
            if m3[(f[3]+2)%8] == m4[(f[4]+6)%8]:
                interface[2] = 0
        # print(interface)

        if num == 1:
            f[1] = (f[1]+d) % 8
            for i in range(len(interface)):
                if interface[i]:
                    d = -d
                    f[i+2] = (f[i+2]+d) % 8
                else:
                    break
        elif num == 2:
            f[2] = (f[2]+d) % 8
            if interface[0]:
                f[1] = (f[1]-d) % 8
            for i in range(1, len(interface)):
                if interface[i]:
                    d = -d
                    f[i+2] = (f[i+2]+d) % 8
                else:
                    break
        elif num == 3:
            f[3] = (f[3]+d)%8
            if interface[2]:
                f[4] = (f[4]-d) % 8
            for i in range(len(interface)-2, -1, -1):
                if interface[i]:
                    d = -d
                    f[i+1] = (f[i+1]+d) % 8
                else:
                    break
        elif num == 4:
            f[4] = (f[4]+d) % 8
            for i in range(len(interface)-1, -1, -1):
                if interface[i]:
                    d = -d
                    f[i+1] = (f[i+1]+d) % 8
                else:
                    break
    res = 0
    if m1[f[1]]:
        res += 1
    if m2[f[2]]:
        res += 2

    if m3[f[3]]:
        res += 4
    if m4[f[4]]:
        res += 8
    print('#%d %d' % (tc, res))





