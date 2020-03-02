import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 1+int(input())):
    N, K = map(int, input().split())
    nums = input()
    print(nums)
    idx = 0
    n = N // 4
    li = []
    while len(li) < K:
        print(idx)
        for i in range(1,5):
            print((idx + n*(i-1))%(N+1), (idx + n*i)%(N+1))
            temp = nums[(idx + n*(i-1))%(N+1):(idx + n*i)%(N+1)]
            # print(temp)
            if temp not in li:
                li.append(temp)
        idx += 1
        print(li)
        # break
        # n1 = nums[:n]
        # n2 = nums[n:2*n]
        # n3 = nums[2*n:3*n]
        # n4 = nums[3*n:4*n]
        # if n1 not in li:

    li.sort()
    print(li[-1])