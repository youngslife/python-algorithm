import sys
sys.stdin = open("5185.txt", "r")

for tc in range(1, 1+int(input())):
    li = input().split()
    arr = li[1]
    arr = arr.replace('0', '0000')
    arr = arr.replace('1', '0001')
    arr = arr.replace('2', '0010')
    arr = arr.replace('3', '0011')
    arr = arr.replace('4', '0100')
    arr = arr.replace('5', '0101')
    arr = arr.replace('6', '0110')
    arr = arr.replace('7', '0111')
    arr = arr.replace('8', '1000')
    arr = arr.replace('9', '1001')
    arr = arr.replace('A', '1010')
    arr = arr.replace('B', '1011')
    arr = arr.replace('C', '1100')
    arr = arr.replace('D', '1101')
    arr = arr.replace('E', '1110')
    arr = arr.replace('F', '1111')

    print('#%d %s' % (tc, arr))

    # N, S = input().split()
    # for i in range(0, int(N)):
    #     t = int(S[i], 16)