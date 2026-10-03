item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
total = round(float(total), 2)

print(f"You have bought {quantity} of {item}.")
print(f"Your total is Rs {total}.")
