import sys
sys.stdin = open("2578.txt", "r")

my = [list(map(int, input().split())) for i in range(5)]
check = []
for i in range(5):
    check += list(map(int, input().split()))

print(my)
print(check)

def row(my):
    for i in range(5):
        for j in range(5):
            if my[i][j] != 0:
                break


def col(my):

def diag(my):

call = 0
for n in check:
    for i in range(5):
        for j in range(5):
            if my[i][j] == n:
                my[i][j] = 0
                if call % 5 == 0:




# # 체크
# for i in range(5):
#     for j in range(5):
#         if check[i][j]

