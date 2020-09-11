import sys
sys.stdin = open("input.txt", "r")

def fine(a, n):
    maxValue = a[0]
    minValue = a[0]
    for i in range(1, n):
        if a[i] > maxValue:
            maxValue = a[i]
        if a[i] < minValue:
            minValue = a[i]
    return maxValue - minValue



T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    res = fine(a, n)
    print("#%d %d" % (tc, res))