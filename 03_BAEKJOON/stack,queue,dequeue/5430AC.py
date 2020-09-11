import sys
sys.stdin = open('input.txt', 'r')
import collections

for tc in range(1, 1+int(input())):
    p = input()
    n = int(input())
    s = input()
    if n == 0:
        arr = []
        if 'D' in p:
            print('error')
            continue
        else:
            print(arr)
            continue
    else:
        arr = collections.deque(list(map(int, s[1:-1].split(','))))
    # print(p)
    # print(arr)
    front = 0
    r = len(arr)-1
    Rcnt = 0
    Dcnt = 0

    for f in range(len(p)):
        # N -= 1
        if p[f] == 'R':
            Rcnt += 1
            front, r = r, front
        elif p[f] == 'D':
            Dcnt += 1
            if Rcnt % 2:
                front -= 1
                if r >= f:
                    print('error')
                    break
            else:
                front += 1
                if f >= r:
                    print('error')
                    break
    else:
        # if Dcnt > n:
        #     print('error')
        if Dcnt == n:
            print('[]')
        # elif front > len(arr)-1 or r > len(arr) -1:
        #     print('error')
        elif front < r:
            print('[', end="")
            for j in range(front, r):
                print(arr[j], end=',')
            print(arr[r], end="")
            print(']')
        elif front == r:
            print('[', end="")
            print(arr[0], end="")
            print(']')

        else:
            print('[', end="")
            for j in range(front, r, -1):
                print(arr[j], end=',')
            print(arr[r], end="")
            print(']')

