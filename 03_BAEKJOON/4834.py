import sys
sys.stdin = open("input3.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input()))
    C = [0] * 10

    for n in range(len(nums)):
        C[nums[n]] += 1
        max_count = max(C)

    for i in range(len(C)):
        if C[i] == max_count:
            max_num = i

    print('#%d %d %d' % (tc, max_num, max(C)))


# def find():
#     maxl = 0
#     for i in range(N):
#         num = int(v[i])
#         card[num] = card[num] + 1
#         if card[maxl] <= card[num]:  # 개수가 더 많은 숫자 카드 추가
#             maxl = max(maxl, num)
#         return maxl





#
# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     nums = list(map(int, input().split()))
#     res = card(nums)
#     print("#%d %d" % (tc, res))
