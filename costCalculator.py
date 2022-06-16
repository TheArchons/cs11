def priceCalc(price):
    print("It will cost ${}".format(round(price*1.12, 2))) # prints the price with the tax added

print("What will you buy?")
print("[a] Salt - $1.40")
print("[b] Pepper - $2.20")
choice = input("Choice: ")

if choice == "a":
    priceCalc(1.40) # calls priceCalc function with the price of Salt as the parameter
else:
    priceCalc(2.20) # calls priceCalc function with the price of Pepper as the parameter