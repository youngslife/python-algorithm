import sys
sys.stdin = open("6190.txt", "r")

# def func(n):
#     for i in range(1, len(str(n))):
#         if str(n)[i-1] > str(n)[i]:
#             return False
#     return True
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#
#     ali = list(map(int, input().split()))
#
#     value = 0
#     for i in range(N):
#         for j in range(i+1, N):
#             n = ali[i] * ali[j]
#
#             func(n)
#
#             if n > value and func(n):
#                 value = n
#
#     if value:
#         print('#%d %d' % (tc, value))
#     else:
#         print('#%d %d' % (tc, -1))



for tc in range(1, int(input())+1):
    n = int(input())
    num = list(map(int, input().split()))
    maxi = -1
    for x in range(n):
        for y in range(x + 1, n):
            k = num[x] * num[y]
            print(k)
            if maxi < k:
                m = k
                check = False
                while m // 10:
                    b = m % 10
                    m //= 10
                    a = m % 10
                    if b < a:
                        check = False
                        break
                    else:
                        check = True
                if check:
                    maxi = k
    print('#%d %d' % (tc, maxi))


