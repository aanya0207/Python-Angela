print("Welcome to tip calculator!")
bill = input("What was the total bill? ")
bill_int = int(bill[1:])
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
person = int(input("How many person to split the bill? "))
amt = ((bill_int * (tip/100)) + bill_int) / person
print(f"Each person should pay : ${amt}")