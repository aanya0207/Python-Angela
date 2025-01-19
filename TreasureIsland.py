print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_=;.______________|_____________________|_______
|                   |  ,-"_,=""     "=.|                  |
|___________________|__"=._o`"-._        "=.______________|___________________
          |                "=._o`"=._      _"=._                     |
 _________|_____________________:=._o "=._."_.-=""=.__________________|_______
|                   |    __.--" , ; "=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-.o`"=._." '. '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`.\` . "-._/_______________|_______
|                   | |o;    `"-.o`"=._``  '` ` `,__.--o;   |
|___________________|_| ;     (#) `-.o`"=.`_.--"o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o..--"    ;o;____/______/_____/_  
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/____/_  
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/_____/_  
/______/______/______/_____/____"=._o._; | ;_.--"o.-"_/______/______/____/_  
____/______/______/_____/_____/____="=._o|o._--""___/______/______/_____/_/_  
/______/______/______/_____/_____/_____/______/______/______/______/_____/_  
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision: Left or Right
choice1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right': ").lower()
if choice1 == "left":
    # Second decision: Swim or Wait
    choice2 = input("You come to a lake. There is an island in the middle. Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    if choice2 == "wait":
        # Third decision: Choose a Door
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        print("One red, one yellow, and one blue.")
        choice3 = input("Which color do you choose? ").lower()
        if choice3 == "red":
            print("🔥 Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("🦁 Eaten by beasts. Game Over.")
            print(" Eaten by beasts. Game Over.")
        elif choice3 == "yellow":
            print("🎉 You found the treasure! You Win!")
        else:
            print("🚪 That's not a valid door. Game Over.")
    else:
        print("🌊 Attacked by a trout. Game Over.")
else:
    print("🕳️ You fell into a hole. Game Over.")
