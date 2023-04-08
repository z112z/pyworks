# 자료구조 - 리스트, 딕셔너리, 튜플, 집합
#인덱싱은 대괄호

# 리스트 - 순서가 정해져 있고, 중복허용
"""
fruit = ['사과', '바나나', '딸기', '바나나'] 
print(fruit)

# 딕셔너리 - 순서가 있고, 키는 중복불가지만 값은 수정 가능

fruit2 = {'사과': '빨강', '바나나': '노랑', '사과': '파랑'} 
print(fruit2)
print(fruit2['사과'])
for key, val in fruit2.items():
    print(key, ':', val)

#튜플 - 순서가 있고, 중복 허용, 값의 수정 삭제 불가
    
t = ('a', 'b', 'c','c')
print(t)
"""

#집합 - 순서가 없고, 중복 불가

s = set() #빈 집합
s.add('사과')
s.add('바나나')
print(s)

#문자열은 1차원 리스트
s2 = {'a', 'b', 'c', 'd', 'b'}
print(s2)

say = "Hello"
print(say)

#문자열을 집합에 포함시킴
say2 = set("Hello")
print(say2)

#중복 제거 
a = [1, 1, 1, 2, 2, 4]

a2 = set(a)
print(a2)

#리스트로 변환
print(list(a2))

# 집합 생성
set1 = {1, 2, 3}
#순서가 없으므로 인덱싱이 안됨 >> 에러남
#print(set1[0])
print(set1)

# 요소 추가
set1.add(4)
print(set1)

#요소 삭제
set1.remove(3)
print(set1)

#요소 존재 확인(True/False)
print(3 in set1)
