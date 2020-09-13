def solution(boxes):
    answer = -1
    boxN = len(boxes)
    dic = {}
    for a, b in boxes:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1

        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1

    couple = 0
    for k, v in dic.items():
        if v % 2 == 0:
            couple += v // 2
        elif v > 2:
            couple += v // 2
            dic[k] = v % 2

    if couple == boxN:
        answer = 0
    else:
        answer = boxN - couple
    return answer
