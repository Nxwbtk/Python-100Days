print("WElcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split_bill = int(input("How many people to split the bill? "))
pay = (bill + ((bill * tip) / 100)) / split_bill
print(f'Each person should pay: ${pay:.2f}')