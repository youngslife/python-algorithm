import sys
sys.stdin = open("bank.txt", "r")

for tc in range(1, 1+int(input())):
    bi = list(input())
    ter = list(input())

    # print(bi)
    n1, n2 = 0, 0

    for i in range(len(bi)):
        if bi[i] == '0':
            bi[i] = '1'
            # print(bi)

            for j in range(len(bi)):
                n1 = n1 + int(bi[j]) * (2 ** ((len(bi) - 1) - j))
            bi[i] = '0'

        elif bi[i] == '1':
            bi[i] = '0'
            # print(bi)
            for j in range(len(bi)):
                n1 = n1 + int(bi[j]) * (2 ** ((len(bi) - 1) - j))
            bi[i] = '1'

        # print('n1', n1)
        f = False
        for j in range(len(ter)):
            # print('1', ter)
            if ter[j] == '2':
                ter[j] = '1'
                # print('2', ter)
                n2 = 0
                for k in range(len(ter)):
                    n2 = n2 + int(ter[k]) * (3 ** ((len(ter) - 1) - k))
                # print('n2', n2)
                if n1 == n2:
                    print('#%d %d' % (tc, n1))
                    f = True
                    break
                else:
                    n2 = 0
                    ter[j] = '0'
                    # print('3', ter)
                    for k in range(len(ter)):
                        n2 = n2 + int(ter[k]) * (3 ** ((len(ter) - 1) - k))
                    # print('n22', n2)
                    if n1 == n2:
                        print('#%d %d' % (tc, n1))
                        f = True
                        break
                ter[j] = '2'
                # print('4', ter)
            elif ter[j] == '1':
                ter[j] = '2'
                # print('6', ter)
                n2 = 0
                for k in range(len(ter)):
                    n2 = n2 + int(ter[k]) * (3 ** ((len(ter) - 1) - k))
                # print('n2', n2)
                if n1 == n2:
                    print('#%d %d' % (tc, n1))
                    f = True
                    break
                else:
                    n2 = 0
                    ter[j] = '0'
                    # print('7', ter)
                    for k in range(len(ter)):
                        n2 = n2 + int(ter[k]) * (3 ** ((len(ter) - 1) - k))
                    # print('n22', n2)
                    if n1 == n2:
                        print('#%d %d' % (tc, n1))
                        f = True
                        break
                ter[j] = '1'
                # print('8', ter)
            elif ter[j] == '0':
                ter[j] = '2'
                n2 = 0
                for k in range(len(ter)):
                    n2 = n2 + int(ter[k]) * (3 ** ((len(ter) - 1) - k))
                # print('n1, n2', n1, n2)
                if n1 == n2:
                    print('#%d %d' % (tc, n1))
                    f = True
                    break
                else:
                    n2 = 0
                    ter[j] = '1'
                    for k in range(len(ter)):
                        n2 = n2 + int(ter[k]) * (3 ** ((len(ter) - 1) - k))
                    # print('n22', n2)
                    if n1 == n2:
                        print('#%d %d' % (tc, n1))
                        f = True
                        break
                ter[j] = '0'
        n1, n2 = 0, 0
        if f:
            break

