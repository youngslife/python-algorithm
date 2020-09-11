import sys
sys.stdin = open('input1.txt', 'r')

def comb(k, s, R):
    global stairs, t, mini

    temp = [0]*len(t)
    for i in range(len(t)):
        temp[i] = t[i]

    if k == R:
        # print('t', t)
        s1 = temp
        s2 = []
        for pp in ppls:
            if pp not in s1:
                s2.append(pp)
        # print('s1', s1)
        # print('s2', s2)
        # print('----------------------')

        for n in range(len(s1)):
            s1[n] = abs(s1[n][0]-stairs[0][0]) + abs(s1[n][1]-stairs[0][1])
        for n in range(len(s2)):
            s2[n] = abs(s2[n][0]-stairs[1][0]) + abs(s2[n][1]-stairs[1][1])
        # print(s2)
        s1.sort()
        s2.sort()
        # print('new', s1)
        # print('new', s2)
        # print('--------------------------------------')
        q1 = [0]*stairs[0][2]
        q2 = [0]*stairs[1][2]
        idx = 0
        # print('q1', q1)
        # print('q2', q2)
        # print('ppls', ppls)

        time = len(q1)+1
        time2 = len(q2)+1
        L2 = len(q2)
        L = len(q1)
        full = 0
        together = 0

        while s1:
            time += 1
            before = time  ###
            if full >= 3:
                # print(idx)
                while idx:
                    time += 1
                    q1[idx % L] = q1[(idx - 1) % L]
                    # print('cccccc', q1)
                    idx = (idx + 1) % L
                    # print(idx)

                full -= together
                # print('full', full)
            # blank = 0

            poplist = []
            floor = []
            for tt in range(3):
                if len(s1) > tt:
                    if before <= s1[tt] <= time:
                        floor.append(s1[tt])
                        # q1[idx % L] = s1[t]
                        poplist.append(tt)
                        full += 1
                        together += 1
            if floor:
                q1[idx] = floor
                idx = (idx + 1) % L
            # if poplist:
            for _ in range(len(poplist)):
                s1.pop(0)
        # print('dddd', s1)
        # print('dddddd', q1)

        full = 0
        together = 0
        idx = 0
        # print('dddd', s2)

        while s2:
            time2 += 1
            before = time2  ###
            if full >= 3:
                # print(idx)
                while idx:
                    time2 += 1
                    q2[idx % L2] = q2[(idx - 1) % L2]
                    idx = (idx + 1) % L2
                    # print(idx)

                full -= together
                # print('full', full)
            # blank = 0

            poplist = []
            floor = []
            for tt in range(3):
                if len(s2) > tt:
                    if before <= s2[tt] <= time2:
                        floor.append(s2[tt])
                        # q1[idx % L] = s1[t]
                        poplist.append(tt)
                        full += 1
                        together += 1
            if floor:
                q2[idx] = floor
                idx = (idx + 1) % L
                print('wwwwwwwwwwwwww', q2)

            for _ in range(len(poplist)):
                s2.pop(0)
            # print(s2)
        # print('final'. q1)
        # print('final', q2)
        # print('final', s1)
        # print(s2)
        #
        # print('time', time, time2)

        if time > time2:
            if mini > time:
                # print('time', time2)
                mini = time
        else:
            if mini > time2:
                # print('time', time)
                mini = time2
        # print('perm', mini)




    else:
        for i in range(s, len(ppls)+(k-R)+1):
            t[k] = ppls[i]
            # print(ppls[i])
            comb(k+1, i+1, R)

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stairs = []
    ppls = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                ppls.append((i, j))
            elif arr[i][j] > 1:
                stairs.append((i, j, arr[i][j]))
    # print(stairs)
    # print(ppls)

    mini = 999999999999999999999

    for n in range(0, len(ppls)+1):
        t = [0]*n
        comb(0, 0, n)
        # print('mini', mini)

    print('res', mini)