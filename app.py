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

    #tip calculator


# def tip_calculate():
#     total_price = float(input("Enter total bill: $"))
#     tip_percent = float(input("Enter tip based on satisfaction: "))
#     tip_amount = (tip_percent / 100) * total_price
#     with_tip = tip_amount + total_price

#     print(f"Tip: ${tip_amount:.2f}")
    
#     # ANSI escape codes
#     RED = "\033[31m"
#     RESET = "\033[0m"  # Reset code to return to default color

#     print(RED + f'Total amount (including tip): ${with_tip:.2f}' + RESET)

# tip_calculate()

# sentence = input("input sentence:")
# word = sentence.split( )
# num_words = len(word)
# print("number of words in sentence is:",num_words)

# number = int(input("input number:"))
# remainder = number % 2
# if remainder == 0:
#     print("even")
# else:
#     print("odd")

def tip_calculate():
     
    tip_percent = {
        'bad': 0.00,
        'okay': 0.15,
        'good': 0.20,
        'amazing': 0.25
    }
        Bill = float(input("enter total bill: $"))
    
    service = input("how was your experience?(bad, okay, good, amazing): ")

if service part of tip_percent
      tip_amount = Bill * tip_percent
      total_amount = tip_amount + Bill

     total_price = float(input("Enter total bill: $"))
     print 
     tip_percent = float(input("bad", "okay", "good", "great"))
     tip_amount = (tip_percent / 100) * total_price
     with_tip = tip_amount + total_price

     print(f"Tip: ${tip_amount:.2f}")