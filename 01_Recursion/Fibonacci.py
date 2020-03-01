# 재귀를 이용한 피보나치 수열

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 2) + fib(n - 1)

# 위의 fib 함수의 시간 복잡도는 O(1)이다.
# basecase와 두개의 재귀호출 모두 input의 크기에 상관없기 때문

# fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))

# 전체 시간 복잡도는 O(2^n)
# 재귀적 실행횟수에 비례한다. 매 호출마다 fib 함수가 재귀적으로 두번 더 호출된다.