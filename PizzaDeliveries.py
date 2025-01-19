print("Welcome to Python Pizza Deliveries!!")
size = input("What size pizza do you want ? S,M or L: ")
pepperoni = input("Do you want pepperoni on your pizza ? y or n : ")
extra_cheese = input("Do you want extra cheese? y or no: ")
bill =0 
if(size == "S"):
    bill+=15
    if(pepperoni == "y"):
        bill+=2
    if(extra_cheese == "y"):
        bill+=1
elif(size == "M"):
    bill+=20
    if(pepperoni == "y"):
        bill+=3
    if(extra_cheese == "y"):
        bill+=1
else:
    bill+=25
    if(pepperoni == "y"):
        bill+=3
    if(extra_cheese == "y"):
        bill+=1
print(f"Your final bill is {bill} ")
            