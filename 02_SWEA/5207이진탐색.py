import sys
sys.stdin = open('5207.txt', 'r')

# dir 0: 몰라, 1: 왼쪽, 2: 오른쪽

def binary(A, low, high, key, dir):
    global cnt
    m = (low + high) // 2
    if low > high:
        return False
    else:
        if dir == 0:
            m = (low + high) // 2
            if key == A[m]:
                return True
            elif key < A[m]:
                return binary(A, low, m-1, key, 1)
            else:
                return binary(A, m+1, high, key, 2)
        elif dir == 1:
            m = (low + high) // 2
            if key == A[m]:
                return True
            elif key < A[m]:
                return False
            else:
                return binary(A, m + 1, high, key, 2)
        elif dir == 2:
            m = (low + high) // 2
            if key == A[m]:
                return True
            elif key < A[m]:
                return binary(A, low, m-1, key, 1)
            else:
                return False

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())  # N의 개수, M의 개수
    A = sorted(list(map(int, input().split())))  # N
    B = list(map(int, input().split()))  # M
    cnt = 0
    for i in range(M):
        if B[i] in A:
            if binary(A, 0, len(A)-1, B[i], 0):
                cnt += 1

    print('#%d %d'%(tc, cnt))