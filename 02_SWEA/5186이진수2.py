import sys
sys.stdin = open("5186.txt", "r")

for tc in range(1, 1+int(input())):
    N = float(input())
    s = ''
    for i in range(1, 14):
        n = 1 / (2 ** i)  # 이부분을 비트로 풀면 더 빨라질 수 있음
        if N >= n:
            N = N - n
            s += '1'
        elif N == 0:
            break
        else:
            s += '0'
    if len(s) > 12:
        print('#%d overflow'%tc)
    else:
        print('#%d %s'%(tc, s))
