# import sys
# sys.stdin = open("input.txt", "r")

# 1단계
new_id = "...!@BaT#*..y.abcdefghijklm"
step1 = new_id.lower()
# step2 = list(step1)
# print(step2)
# 2단계
for i in '~!@#$%^&*()=+[{]}:?,<>':
    if i in step1:
        step1 = step1.replace(i, '')
answer = ''
# 3단계
answer += step1[0]
print(step1)
for i in range(1, len(step1)):
    if step1[i] == '.':
        if step1[i-1] == '.':
            continue
    answer += step1[i]
print(answer)
    

step2 = list(step1)
temp = []
for i in range(1, len(step2)):
    if step2[i] == '.':
        if step2[i-1] == '.':
            temp.append(i-1)
for i in range(len(temp)-1, -1, -1):
    step2.pop(temp[i])
print(temp)
print(step2)
# 4단계
while step2[0] == '.' or step2[-1] == '.':
    if step2[0] == '.':
        step2.pop(0)
    if step2[-1] == ',':
        step2.pop()
print(step2)






# def solution(new_id):
#     answer = ''
#     # 1단계
#     step1 = new_id.lower()
#     # 2단계
#     for i in '~!@#$%^&*()=+[{]}:?,<>':
#         if i in step1:
#             step1 = step1.replace(i, '')
#     # 3단계
#     answer += step1[0]
#     for i in range(1, len(step1)):
#         if step1[i] == '.':
#             if step1[i-1] == '.':
#                 continue
#         answer += step1[i]

#     # 4단계
#     while answer[0] == '.' or answer[-1] == '.':
#         if answer[0] == '.':
#             answer = answer[1:]
#         if answer[-1] == '.':
#             answer[:-1]
#     # 5단계
#     if not answer:
#         answer = 'a'
#     # 6단계
#     if len(answer) >= 16:
#         answer = answer[:15]
#         for i in range(len(answer)-1, -1, -1):
#             if answer[i] != '.':
#                 answer = answer[:i+1]
#                 break
#     # 7단계
#     while len(answer) < 3:
#         answer += answer[-1]

#     return answer