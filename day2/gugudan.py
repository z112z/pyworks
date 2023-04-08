# 구구단

dan = int(input("단을 입력하세요.: "))
result_val =""
for i in range(1, 10):
    #print(dan * i)
    #print(f'{dan} x {i} = {dan * i}')
    current_val = f'{dan} x {i} = {dan * i}\n' #\n - 줄바꿈, 이스케이프 문자
    result_val = result_val + current_val #result_val += current_val
print(result_val)


# 중첩 for문
"""
for i in range(5): #0, 1, 2, 3, 4 #range(0,5)해도 됨
    for j in range(5):
        print('*', end='')
    print()  # 줄바꿈
"""

"""
for i in range(0, 5): 
    for j in range(0, 5-i): #range(0, i+1)
        print('*', end='')
    print()  
"""

"""
# 전체 구구단(2~9단)
start_dan = int(input("시작단 입력: "))
end_dan = int(input("끝단 입력: "))

for i in range(start_dan, end_dan + 1): #end_dan 에는 +1해줘야 됨.
    for j in range(1,10):
        print(f'{i} X {j} = {i*j}')
    print()
"""
