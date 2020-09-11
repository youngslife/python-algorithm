import sys
sys.stdin = open('5204.txt', 'r')


def merge(left, right):
    global cnt
    result = [0]*(len(left)+len(right))
    # print('22', result)
    i = 0
    j = 0
    k = 0
    # print('merge', left)
    # print('merge', right)
    if left[-1] > right[-1]:  # 두 그룹을 병합하기 전에 count
        cnt += 1

    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1
        # print('result', result)
    if len(left) > i:
        result = result[:k]
        result += left[i:]
    if len(right) > j:
        result = result[:k]
        result += right[j:]

    return result


def merge_sort(li):
    if len(li) == 1:
        return li

    # middle = len(li) // 2
    # left = li[:middle]
    # right = li[middle:]
    # left = merge_sort(left)
    # right = merge_sort(right)

    left = merge_sort(li[:len(li)//2])
    right = merge_sort(li[len(li)//2:])

    return merge(left, right)


for tc in range(1, 1+int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    res = merge_sort(nums)
    # print(res)
    print('#%d %d %d' % (tc, res[N//2], cnt))
