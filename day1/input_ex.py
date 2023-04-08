#입력 함수 - input()

"""
print("문자 입력: ")
text= input()
print(text)
"""
'''
#단축 표현문
text = input("문자 입력: ")
print(text)
'''
    
"""
#숫자 입력
num = input("숫자 입력 : ") #num은 문자임
num = int(num)  #int()함수로 숫자로 변환함
print(num - 10)
"""
'''
#단축표현법
num = int(input("숫자 입력 : "))
print(num -10)
'''

'''
#문자열 더하기
print("대한" + "민국")

#문자열 곱하기
print("=" * 10)
print("지구"*3)
'''


#이름은 홍길동입니다.
#나이는 30세입니다.

name = input("이름: ")
print("이름은 " + text + "입니다.")
age = input("나이: ")
print("나이는"+ age +"세 입니다.")

#age = int(input("나이: "))
#print("나이는"+ str(age) +"세 입니다.") 이렇게 해야 오류 안남. 아까 str 안붙여서 오류 겁나 뜸
