# 좌석 배치
customer = int(input("입장객 수 입력 : ")) #입장객
col_num = int(input("좌석 열 수 입력 : "))   #좌석 열
row_num = 0;  #줄수 row_num; 이렇게 써도 됨, 생략 가능

if customer % col_num == 0:
    #row_num = int(customer / col_num)
    row_num = customer // col_nem #파이썬에서는 이렇게 써도 됨
else:
    row_num = int(customer / col_num) + 1

#print(str(row_num) + "줄이 필요합니다.")
#print(f'{row_num}줄이 필요합니다.') #f String 방식
#print("{}줄이 필요합니다.".format(row_num))

for i in range(0,row_num):
    for j in range(1,col_num+1):
        #좌석번호가 고객번호보다 클 때 빠져나옴
        seat_num = (col_num*i)+j
        if seat_num > customer:
            break
        #print("좌석" + str(seat_num), end =' ')
        print(f'좌석{seat_num}', end=" ")
    print()
