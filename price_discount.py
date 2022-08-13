"""
A store is doing a bonanza, who ever buys goods less than or equal to
500 Naira will get 10% discount, anyone buying goods above 500 but less than
 N1000 gets a 15% discount, and goods of N1000 above has 20% discount.
 Write a program that prints the amount a buyer will pay for each purchase.
"""

price_goods = int(input("Enter the Price: "))
discount_1 = price_goods * 0.1
discount_2 = price_goods * 0.15
discount_3 = price_goods * 0.2

if price_goods <= 500:
    pay_amount = price_goods - discount_1
elif price_goods > 500 and price_goods < 1000:
    pay_amount = price_goods - discount_2
else:
    pay_amount = price_goods - discount_3
print("you are to pay: ", pay_amount)

