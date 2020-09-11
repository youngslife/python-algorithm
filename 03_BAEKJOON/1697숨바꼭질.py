import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
cnt = 0
visited = [0]*100001

if N == K:
    print(0)
else:
    q = [N]
    visited[N] = 1
    f = False

    while q:
        for _ in range(len(q)):
            sb = q.pop(0)

            if sb == K:
                f = True
                break
            if 0 <= sb * 2 <= 100000 and not visited[sb * 2]:
                q.append(sb * 2)
                visited[sb * 2] = 1
            if 0 <= sb - 1 <= 100000 and not visited[sb - 1]:
                q.append(sb - 1)
                visited[sb - 1] = 1
            if 0 <= sb + 1 <= 100000 and not visited[sb + 1]:
                q.append(sb + 1)
                visited[sb + 1] = 1

        if f:
            break
        cnt += 1

    print(cnt)