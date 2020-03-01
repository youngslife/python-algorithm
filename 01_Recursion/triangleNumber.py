# 숫자합 삼각수

# 1부터 n까지의 합을 리턴
def triangle_number(n):
    if n == 1:
        return 1
    return n + triangle_number(n-1)

# triangle_number(1)부터 triangle_number(10)까지 출력
for i in range(1, 11):
    print(triangle_number(i))


# 함수가 총 n번 호출되니까, 시간복잡도는 O(n)