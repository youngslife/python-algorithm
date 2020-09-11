import sys
sys.stdin = open("5097.txt", "r")


def enq(item):
    global r
    if isFull():
        print('full')
    else:
        r = (r+1) % len(q)
        q[r] = item


def deq():
    global f
    if isEmpty():
        print('Empty')
    else:
        f = (f+1) % len(q)
        return q[f]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    q = [0]*(N+1)
    f = r = 0

    for i in nums:
        enq(i)

    for i in range(M):
        deq()
        enq(q[f])

    print('#%d %d'%(tc, q[(f+1)%len(q)]))
