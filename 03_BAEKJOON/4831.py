import sys
sys.stdin = open("input2.txt", "r")


def ebus(K, N, M, charger):
    stations = [0] * (N + 3)
    for j in range(len(charger)):
        stations[charger[j]] += 1
    count = 0
    start = 0
    stop = 0

    while start < N + 1 and stop == 0:
        if stations[start + K] == 1:
            start = start + K
            count += 1
        else:
            for i in range(K, -1, -1):
                if start + i == N:
                    start += i
                    stop = 1
                    break
                elif i == 0:
                    stop = 1
                    count = 0
                    break
                elif stations[start + i] == 1:
                    start = start + i
                    count += 1
                    break

    return count



T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    res = ebus(K, N, M, charger)
    print("#%d %d" % (tc, res))