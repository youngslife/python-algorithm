import sys
sys.stdin = open("2005.txt", "r")

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [[1]+[0]*N for _ in range(N)]


    for i in range(1, N):
        for j in range(1,N):
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]

    print('#%d'%(tc))
    for i in range(N):
        for j in range(i+1):
            print(arr[i][j], end=" ")
        print()
