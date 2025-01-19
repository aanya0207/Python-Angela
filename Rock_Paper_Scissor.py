# Import Libraries
import random
# Game visualizations
game =[]
rock= ''' 
       ____
------(____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
game.append(rock)
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
game.append(paper)
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game.append(scissor)

#intro 
print("Welcome to Rock,Paper and Scissor")
# Input Users choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if(0<=user_choice<3):
    print(game[user_choice])
else:
    print("Invalid input")
# Computers choice
comp_choice = random.randint(0,2)
print(f'Computers choice : \n {game[comp_choice]}')

if(user_choice ==comp_choice):
    print("It's Draw")
elif(user_choice == 0 and comp_choice == 2):    # Rock wins against scissor
    print("You win!")
elif(user_choice == 2 and comp_choice == 1):    # Scissor wins against paper
    print("You win!")
elif(user_choice == 1 and comp_choice == 0):    # Paper wins against rock
    print("You win!")
else:
    print("You lose!")
