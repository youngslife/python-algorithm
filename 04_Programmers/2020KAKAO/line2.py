def solution(ball, order):
    answer = []
    while ball:
        for i in range(len(order)):
            if ball[0] == order[i]:
                answer.append(ball.pop(0))
                order.pop(i)
                break
            elif ball[-1] == order[i]:
                answer.append(ball.pop())
                order.pop(i)
                break
            
    return answer