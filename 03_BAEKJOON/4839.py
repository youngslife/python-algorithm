import sys
sys.stdin = open("input4839.txt", "r")

def page(low, high, key, cnt):
    c = (low + high) // 2
    cnt += 1
    if key == c:
        return cnt
    elif key < c:
        return page(low, c, key, cnt)
    elif c < key:
        return page(c, high, key, cnt)

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    start = 1
    end = P
    count = 0

    a = page(start, end, Pa, count)
    b = page(start, end, Pb, count)

    if a > b:
        print('#%d B' % tc)
    elif a < b:
        print('#%d A' % tc)
    elif a == b:
        print('#%d 0' % tc)


# T = int(input())
#
# for tc in range(1, T+1):
#     P, Pa, Pb = map(int, input().split())
#
#     low = 1
#     high = P
#
#
#     while start <= r:
#         c = (start+r)//2
#         if c == Pb:
#             B += 1
#             break
#         elif c > Pb:
#             r = c - 1
#             B += 1
#         else:
#             start = c + 1
#             B += 1
#
#     start = 1
#     r = P
#
#     while start <= r:
#         c = (start+r)//2
#         if c == Pa:
#             A += 1
#             break
#         elif c > Pa:
#             r = c - 1
#             A += 1
#         else:
#             start = c + 1
#             A += 1
#
#     if A == B:
#         print('#%d 0' % tc)
#     elif A > B:
#         print('#%d B' % tc)
#     else:
#         print('#%d A' % tc)