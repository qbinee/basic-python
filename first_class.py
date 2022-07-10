# 일급함수
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과 반환 가능(return)

# 함수 객체
def factorial(n):
    """ factorial function
    :param n: int
    :return:
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(factorial.__doc__)

