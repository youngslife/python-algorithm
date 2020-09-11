import sys
sys.stdin = open("4866.txt", "r")

T = int(input())
for tc in range(1, T+1):
    s = input()

    stack = []

    # for i in s:
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{':
            stack.append(s[i])
        elif s[i] == ')' or s[i] == '}':
            if len(stack) == 0:
                result = 0
                break
            else:
                if s[i] == ')':
                    t = stack[-1]
                    stack.pop(-1)
                    if t == '(':
                        continue
                    else:
                        result = 0
                        break
                elif s[i] == '}':
                    t = stack[-1]
                    stack.pop(-1)
                    if t == '{':
                        continue
                    else:
                        result = 0
                        break
    else:
        if len(stack) == 0:
            result = 1
        else:
            result = 0

    print('#{} {}'.format(tc, result))


            # def check(s):
            #     for i in range(len(s)):
            #         if s[i] == '(':
            #             stack.append(s[i])
            #             # stack[top+1] = i
            #         elif s[i] == ')':
            #             if len(stack) == 0:
            #                 return ('fail')
            #             else:
            #                 t = stack[-1]
            #                 stack.pop(-1)
            #                 if t == '(':
            #                     continue
            #                 else:
            #                     return ('fail')
            #     return ('success')
