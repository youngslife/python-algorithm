import sys
sys.stdin = open('1.txt', 'r')

for tc in range(1, 1+int(input())):
    info, N = input().split()
    N = int(N)
    nums = list(map(int, info))
    # print('ori', nums)
    cnt = 0

    for i in range(len(nums)-1):
        smallN = 0
        max = nums[i]
        maxid = i
        maxidlist = []
        # print(max, maxidlist)
        for j in range(len(nums)-1, i, -1):
            if nums[i] > nums[j]:
                smallN += 1
                # print('sm', smallN)

            elif nums[i] < nums[j]:
                if nums[j] > max:
                    max = nums[j]
                    if maxidlist:
                        maxidlist.pop(-1)
                    maxidlist.append(j)
                    # print(maxidlist)
                elif nums[j] == max:
                    maxidlist.append(j)
            # else:
            #     maxidlist.append(j)
                # print(maxidlist)

        # print(max, maxidlist)
        if not maxidlist:
            continue

        else:
            if len(maxidlist) > smallN:
                maxid = maxidlist[smallN]
                nums[i], nums[maxid] = max, nums[i]
                cnt += 1
                # print(cnt)
                # print(nums)
                if cnt == N:
                    break
            else:
                maxid = maxidlist[0]
                nums[i], nums[maxid] = max, nums[i]
                cnt += 1
                # print(cnt)
                # print(nums)
                if cnt == N:
                    break
    while cnt < N:
        if nums[-2] > nums[-1]:
            for i in range(len(nums)-3, -1, -1):
                if nums[i] <= nums[-2]:
                    nums[-2] = nums[i]
                    cnt += 1
                    break
            else:
                nums[-2], nums[-1] = nums[-1], nums[-2]
                cnt += 1
            if cnt == N:
                break
        else:
            nums[-2], nums[-1] = nums[-1], nums[-2]
            cnt += 1
        if cnt == N:
            break

    print('#%d'%tc, end=" ")
    print(''.join(map(str, nums)))
        # else:
        #     nums[-2], nums[-1] = nums[-1], nums[-2]



    # for i in range(len(nums)-1):
    #     max = nums[i]
    #     maxid = i
    #     print(max, maxid)
    #     for j in range(i+1, len(nums)):
    #         if nums[i] <= nums[j]:
    #             if nums[j] >= max:
    #                 max = nums[j]
    #                 maxid = j
    #     print(max, maxid)
    #     if maxid == i:
    #         continue
    #
    #     else:
    #         nums[i], nums[maxid] = max, nums[i]
    #         cnt += 1
    #         print(cnt)
    #         print(nums)
    #         if cnt == N:
    #             break
    # while cnt < N:
    #     if nums[-2] > nums[-1]:
    #         for i in range(len(nums)-3, -1, -1):
    #             if nums[i] <= nums[-2]:
    #                 nums[-2] = nums[i]
    #                 cnt += 1
    #                 break
    #         else:
    #             nums[-2], nums[-1] = nums[-1], nums[-2]
    #             cnt += 1
    #         if cnt == N:
    #             break
    #     else:
    #         nums[-2], nums[-1] = nums[-1], nums[-2]
    #         cnt += 1
    #     if cnt == N:
    #         break

