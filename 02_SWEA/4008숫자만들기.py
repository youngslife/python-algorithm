import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 1+int(input())):
    N = int(input())
    p, m, s, d = map(int, input().split())
    nums = list(map(int, input().split()))
    