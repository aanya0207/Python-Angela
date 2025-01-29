import random
EASY = 10
HARD = 5
def play_game(n):
    num = random.randint(1,101)
    cnt=0
    while n>=0 :
        print(f"You have {n} attempts remaining to guess the number. ")
        n-=1
        guess = int(input("Make a guess: "))
        if(guess == num):
            cnt+=1
            print(f"You got it! The answer was {num} .")
            break
        elif(guess == num+1 or guess == num-1):
            print("Close" and n==10)
            print("Guess again")
        elif(guess<num):
            print("Too low.")
            print("Guess again.")
        else:
            print("Too high.")
            print("Guess again.")
    
    if(cnt == 0):
        print(" You run out of turns. You lost.")

logo = r'''
  ________                               _______               ___.                 
 /  _____/ __ __   ____   ______ ______  \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/  /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/          \/            \/    \/     \/                                                                                                                                                                                                                                               

'''
print(logo)

print("Welcome To The Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100. ")
ch = input("Choose a difficulty. Type 'easy' or 'hard' : ")
if ch == 'easy':
    play_game(EASY)
else:
    play_game(HARD)
print("Goodbye!!")