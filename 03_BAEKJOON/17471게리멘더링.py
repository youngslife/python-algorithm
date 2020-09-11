import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
ppls = list(map(int, input().split()))
map = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    infos = list(map(int, input().split()))
    idx = 1
    for _ in range(idx[0]):

