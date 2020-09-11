import sys
sys.stdin = open("3752.txt", "r")

def powersetlist(s):
    r = [[]]

    for e in s:
        temp = [x+[e] for x in r]
        r += temp
    return r

for tc in range(1, 1+int(input())):
    N = int(input())
    nums = list(map(int, input().split()))

    ps = powersetlist(nums)

    final = []

    for i in range(len(ps)):
        final.append(sum(ps[i]))

    print('#%d %d' % (tc, len(set(final))))


    # print('#%d %d'%(tc, len(set(Nsum))))


#
# def power_set_r(k):
#     global Nsum
#     if k == N:
#         # print(a)
#         total = 0
#         for i in range(len(a)):
#             if a[i] == 1:
#                 total += nums[i]
#         Nsum.append(total)
#     else:
#         a[k] = 1
#         power_set_r(k + 1)
#         a[k] = 0
#         power_set_r(k + 1)
#
#
# for tc in range(1, 1+int(input())):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     print(nums)
#     a = [0]*N
#     Nsum = []
#     power_set_r(0)
#
#     print('#%d %d'%(tc, len(set(Nsum))))

# sys.stdout = open("testout.txt", "w")
# import time
# 인풋값 받기 전에 stime = time.time()
# 종료하고 print(time.time()-stime)



