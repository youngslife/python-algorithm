import sys
sys.stdin = open("input4868.txt", "r")

T = int(input())

for tc in range(1 ,T+1):
    str1 = input()
    str2 = input()

    P = len(str1)
    T = len(str2)

    i = 0
    j = 0
    while j < P and i < T:
        if str2[i] != str1[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == P:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))