import sys
sys.stdin = open("input4865.txt", "r")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    info = {}

    for i in range(len(str1)):
        info[str1[i]] = str2.count(str1[i])

    Max = info[str1[0]]
    for k, v in info.items():
        if Max < v:
            Max = v

    print('#{} {}'.format(tc, Max))

# count = {}.fromkeys(str1, 0)