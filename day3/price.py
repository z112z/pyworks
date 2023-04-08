#배송비 계산하기
# 주문가격이 20000원 미만이면 배송비(2,500원)를 포함하고, 이상이면
#배송비를 포함하지 않는 프로그램
# 단위가격, 수량 - 매개변수

def get_price(unit_price, quantity):
    fee = 2500 #배송비
    price = unit_price * quantity #주문가격 = 단위가격 x 수량
    if price < 20000:
        price += fee
    else:
        price
    return price

money1 = get_price(15000, 2) #주문 금액 = get_price()
money2 = get_price(15000, 1)
print("주문금액 : {}원".format(money1))
print("주문금액 : {}원".format(money2))
