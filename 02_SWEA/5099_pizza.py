import sys
sys.stdin = open("5099.txt", "r")


def isEmpty():
    return f == r


def isFull():
    return (r+1) % len(q) == f


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
        if q[f][1] == 1:
            return [q[f][0], 0]
        else:
            q[f][1] -= q[f][1]//2
            return q[f]


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = [0] + list(map(int, input().split()))

    q = [0]*(N+1)
    f = r = 0
    print(q)
    print('-------')

    for i in range(1, N+1):
        enq([i, cheese[i]])
    print(q)
    print('----------')

    for i in range(N+1, len(cheese)+1):
        print('i:', i)
        for j in range(100):
            if isFull():
                check = deq()
                print('check:', check)
                if check[1] == 0:
                    if i == len(cheese):

                        print('qqqq', q)
                        print('r:', q[f])
                        print(check[0])
                        break
                    else:
                        print('new:', cheese[i])
                        enq([i, cheese[i]])
                        print('new q:', q)
                        break
                else:
                    enq(q[f])
                    print('q:', q)
    print('result:', q[f])



    # for i in range(100):
    #     if isFull():
    #         check = deq()
    #         print(check)
    #         if check == 0:
    #             for i in range(N+1, len(cheese)):
    #                 print('new:', cheese[i])
    #                 enq(cheese[i])
    #                 print('new q:', q)
    #                 break
    #         else:
    #             enq(q[f])
    #             print(q)


