# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    if len(some_list) == 1 or len(some_list) == 0:
        return some_list
    return [some_list[-1]] + flip(some_list[:-1]) # 이부분 시간 복잡도 O(n-1)



some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# flip 함수가 재귀적으로 n번 실행되므로
# 전체 시간복잡도 O(n^2)