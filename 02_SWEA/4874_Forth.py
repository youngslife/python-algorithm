import sys
sys.stdin = open("4874.txt", "r")

def calculate(n1, n2, o):
    if o == '+':
        return n1 + n2
    elif o == '-':
        return n1 - n2
    elif o == '*':
        return n1 * n2
    elif o == '/':
        return n1 // n2


T = int(input())
for tc in range(1, T+1):
    stack = [0]*256
    top = -1
    s = input().split()

    operator = ['+', '-', '/', '*']

    for i in range(len(s)):
        if s[i] == '.':
            if top > 0:
                print('#%d error' % tc)
                break
            else:
                res = stack[top]
                print('#%d %d' % (tc, res))
                break
            # else:
            #     print('#%d error' % tc)
            #     break
        elif s[i] not in operator:
            stack[top+1] = s[i]
            top += 1
        else:
            if top >= 1:
                t2, t1 = int(stack[top]), int(stack[top-1])
                stack[top], stack[top-1] = 0, 0
                top -= 1
                stack[top] = calculate(t1, t2, s[i])
            else:
                print('#%d error'%tc)
                break


