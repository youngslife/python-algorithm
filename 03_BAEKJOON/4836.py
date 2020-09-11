import sys
sys.stdin = open("input4836.txt", "r")

T = int(input())

for tc in range(1, T+1):
    box = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for _ in range(box):
        data = list(map(int, input().split()))
        row = data[:-1:2]
        col = data[1::2]
        color = data[-1]

        for i in range(row[0], row[1]+1):
            for j in range(col[0], col[1]+1):
                arr[i][j] += color

    count = 0
    for i in range(len(arr)):
        for j in arr[i]:
            if j == 3:
                count += 1
    print('#%d %d' % (tc, count))
    count = 0
