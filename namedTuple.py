# 객체 -> 파이썬 데이터 추상화
# 모든 객체 -> type , id -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# print(l_leng1)

# named tuple
from collections import namedtuple

Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3.x, pt4)

l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)
# print(l_leng2)

# 네임드 튜플 선언 방법 -> 숙지하기
Point1 = namedtuple('Point', ['x', 'y'])  # 위와 동일
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y x class', rename=True)  # defalut = false -> 예약어 무시

# print(Point3)

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 30)

# _asdict() : OrderedDict 반환 -> named tuple을 dic으로 반환
# print(p1._asdict())
# print(p2._asdict())


# 실사용 실습
# 반20명 4개의 반 (A, B, C, D)
# named tuple로 구성

Classes = namedtuple('classes', ['rank', 'number'])

numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# List Comprehension -> 진행형 리스트
students = [Classes(rank, number) for rank in ranks for number in numbers]

# print(len(students))
# print(students)
# named tuple 은 collects (집합)이다

# 추천 !
students2 = [Classes(rank, number)
             for rank in 'A B C D'.split()
             for number in [str(n)
                            for n in range(1, 21)]]
# tuple -> 내용 변경 불가!
# 모델링 -> json 
