import sys
sys.stdin = open("sc0911.txt", "r")

code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    c = ''
    f = False
    for i in range(len(arr)):
        s = arr[i]
        for j in range(len(s)-1, -1, -1):
            if s[j] == '1':
                l = s[j-55:j+1]
                for k in range(0, len(l), 7):
                    new = l[k:k+7]
                    for m in range(len(code)):
                        if new == code[m]:
                            c += str(m)
                f = True
                break
            else:
                continue
        if f:
            break

    check = 0
    for i in range(0, len(c)-1, 2):
        check += 3*int(c[i]) + int(c[i+1])
    if check % 10 == 0:
        res = 0
        for i in c:
            res += int(i)
    else:
        res = 0

    print('#%d %d'%(tc, res))
