# x = 3
# y = float(3)
# print(x,y)

import string
#do this later
# print("poop")
# unless:input==0 print("no poop")


# val = [1,2,3,4,5,6,7,8,9,10,300]
# for i in val: 
#     print (val[6])
#     print(val[5])


def tip_calculate():
    total_price = float(input("enter total bill: $"))
    tip_precent = float(input("enter tip based on satisfaction: "))
    tip_amount = (tip_precent / 100) * total_price
    With_tip = tip_amount + total_price
    print(f"Tip precent: ${tip_precent:.2f}")
    print(f'total amount (including tip): {With_tip:.2f}')

tip_calculate()
