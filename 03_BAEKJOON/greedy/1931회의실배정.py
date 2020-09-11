import sys
sys.stdin = open('input.txt', 'r')

# 133804 KB / 564 ms
N = int(input())
table = []

for i in range(N):
    s, e = map(int, input().split())
    table += [[e, s]]

table.sort()

e1, s1 = table.pop(0)
cnt = 1

for e2, s2 in table:
    if s2 < e1:
        continue
    else:
        e1 = e2
        cnt += 1
print(cnt)


# 128460 KB / 568 ms
N = int(input())
table = []

for i in range(N):
    s, e = map(int, input().split())
    table += [(e, s)]

table.sort()

e1, s1 = table.pop(0)
cnt = 1

for e2, s2 in table:
    if s2 < e1:
        continue
    else:
        e1 = e2
        cnt += 1
print(cnt)



# 126484 KB / 568 ms
N = int(input())
table = [0 for _ in range(N)]

for i in range(N):
    s, e = map(int, input().split())
    table[i] = (e, s)

table.sort()

e1, s1 = table.pop(0)
cnt = 1

for e2, s2 in table:
    if s2 < e1:
        continue
    else:
        e1 = e2
        cnt += 1
print(cnt)