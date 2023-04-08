# 파일 이름(모듈) - var.py
# 변수 만들기(선언)

#여러 줄 주석 - 쌍따,홑따옴표 세번 붙여줌

# 변수이름 만들때 주의할 점
#1. 숫자로 시작하면 에러 발생(EX. 3user)
#2. 변수이름에 공백이 들어가면 에러 발생
#ex.3사 계절 = '봄'
#print(사 계절)

'''
user = "sky2003"#아이디 넣으면 됨 따옴표안에
password = "abc1234"

print(user)
print(password)

print("아이디:",user)
print("비밀번호:",password) #콤마 한칸

# 사칙연산(변수 이용)
num1 = 12
num2 = 5

print(num1 + num2)
print("더하기:", num1 + num2) #17
print("빼기:", num1 - num2) #7
print("곱하기:", num1 * num2) #60
print("나누기:", num1 / num2) #2.4
print("나머지:", num1 % num2) #2
print("몫:", num1 // num2) #2(파이썬만 있음)
'''

# 총점과 평균
#다른 언어는 int,float 타입을 앞에 붙여야됨
eng = 70    #eng 변수에 70을 대입
math = 80   #math라는 변수에 80을 대입
total = eng + math  #총점 = 영어 + 수학점수
print(total)

avg = total / 2 #평균 = 총점 / 개수
print(avg)

print(type(total))  #type()함수는 자료형을 알려줌
print(type(avg))

#bool 자료형(논리)
state = False
print(state)
print(type(state))

#> < ==
print(3==2) #False
print(3>2)  #True


