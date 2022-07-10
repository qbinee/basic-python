# 번호가 붙은 자료형
# 시퀀스형에 관하여
# 컨테이너(Container : 서로다른 자료형 [List, tuple, collections, deque])
# 풀랫(Flat : 한개의 자료형( str, byte, bytearray, array, memoryview])
# 가변(list, byterray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# list , tuple 고급

# 지능형 리스트(Comprehending lists)
chars = '+_)(*&^%$#@!'
code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))
# print(code_list1)

# 지능형 리스트(Comprehending lists)
code_list2 = [ord(s) for s in chars]

# print(code_list2)



# Comprehending Lists + Map, Filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
# filter -> 데이터 전처리에 좋다.
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))

# print(code_list3)
# print(code_list4)
# print([chr(s) for s in code_list4])


# Generator 생성
# 수치 연산의 최적을 가지고 있다.
import array

# Generator : 한번에 한개의 항목을 생성 ( 메모리 유지x )
# 메모리 할당을 아낄 수 있다는 장점이 있다.
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))
print(tuple_g)  # <generator object <genexpr> at 0x10457c3c0> -> 아직 값 생성 안함

print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))

print(array_g)
print(type(array_g))
print(array_g.tolist())

print()
print()

# generator example
print(('%s' % c + str(n) for c in ['a', 'b', 'c', 'd'] for n in range(1, 21)))

for s in ('%s' % c + str(n) for c in ['a', 'b', 'c', 'd'] for n in range(1, 21)):
    # 하나 생성하고 하나 출력하고
    print(s)

print()
print()
# 리스트 주의

marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~']*3] * 4 # 이거는 같은 주소값을 복사
print(marks1)
print(marks2)

# 수정
marks1[0][1] = 'x'
marks2[0][1] = 'x'
print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1]) #print : [4371816896, 4371816768, 4371816704, 4371816576]
print([id(i) for i in marks2]) #print: [4371816512, 4371816512, 4371816512, 4371816512]

# for i in marks2:
#     for j in i:
#         print(id(j), end=' ')
#     print()


# Tuple advanced
# Unpacking

# b, a = a, b
print(divmod(100, 9))
# ()로 묶인것은 1개이지 때문에 아스타 * 로 풀어서 넣어야 실행이 가능하다.
print(divmod(*(100, 9)))
# 결과 값 또한 tuple()이기 때문에 * (unpacking) 실행
print(*(divmod(100, 9)))

print()

x, y, *rest = range(10)

print(rest)

# Mutable (가변) Immutable(불변)
l = (15, 20, 25)
m = [15, 20, 25]
print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2
print(l, id(l)) # 아이디 재할당
print(m, id(m))

# sort vs sorted
# reverse, key=Len, key=str.Loser, key=func

# sorted: 정렬 후 새로운 객체 반환
# sort : 정렬후, 객체 직접 반환

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon']
print('sorted -', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key=lambda x: x[-1]))


print(f_list)

# sorted : 정렬 후 객체 직접 변경
# 반환 값 확인(None)
print('sort -', f_list.sort(), '원본 수정됨', f_list)

# List vs Array 적합한 사용성 설명
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반: ai 기계학습, 고속연산, 배열(리스트와 거의 호환)

# 해시 테이블
# 해시 값이 중복될떄 처리를 어떻게 하는가?
# key에 value를 저장하는 구조 __dict__
# 파이썬 dict = 해쉬테이블
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 => 해쉬 주소 -> key에 대한 value 참조

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
print(hash(t1)) # 튜플은 해쉬값이 추출 가능하다.

# Dict SetDefalut 예제
source = (('k1', 'val1')
          ,('k1', 'val2')
           ,('k2', 'val3')
           ,('k2', 'val4')
           ,('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# no use Setdefault
for k, v in source:
    print('print', k, [v])
    if k in new_dict1:
        # 이후 있는 곳에 값만 넣어주기
        new_dict1[k].append(v)
    else:
        # 없으면 리스트 새로 생성
        print(k, [v])
        new_dict1[k] = [v]

print(new_dict1)

# use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k: v for k, v in source}
print(new_dict3) # 안돼용

# dict 및 set 추가

# immutanle Dict

from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))


# 수정 가능
d['key2'] = 'value2'

print(d)

# 수정 불가능
# d_frozen['key2'] = 'value2'
#
# print(d_frozen)


# set
s1 = {'apple', 'orange', 'apple', 'orange', 'kiwi'}
s2 = set(['apple', 'orange', 'apple', 'orange', 'kiwi'])
s3 ={3}
s3 = set() # not {}
s5 = frozenset({'apple', 'orange', 'apple', 'orange', 'kiwi'})

# s1.add('melon')
# print(s1)

# 선언 최적화
# 바이트코드실행 -> i파이썬 인터프리터 실행
from dis import dis

print('--------')
print(dis('{10}'))

# 지능형 집합 (comprehending set)

print('-----')

from unicodedata import name

print({name(chr(i), '') for i in range(0, 256)})