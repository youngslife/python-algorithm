import sys
sys.stdin = open("4873.txt", "r")


T = int(input())
for tc in range(1, T+1):
    s = input()

    stack = []

    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:
                stack.pop(-1)
            elif s[i] != stack[-1]:
                stack.append(s[i])

    print('#%d %s' % (tc, len(stack)))

