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