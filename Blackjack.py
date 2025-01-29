import random
# Define the logo as a raw string variable
logo = r'''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/ 
'''

# Function to print the logo
def print_logo():
    print(logo)

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u,c):
    if u == c:
        return "Draw 🙃"
    elif c == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u == 0:
        return "Win with a Blackjack 😎"
    elif u > 21:
        return "You went over. You lose 🥲"
    elif c > 21:
        return "Opponent went over. You win 😇"
    elif u>c:
        return "You win 🙂"
    else:
        return "You lose 😤"



def play_game():
    user_card = []
    comp_card = []
    curr_comp_score =-1
    
    for i in range(2):
        new_card = deal_card()
        user_card.append(new_card)
        comp_card.append(new_card)

    is_game_over = False
    curr_score = calculate_score(user_card)
    curr_comp_score = calculate_score(comp_card)
    print(f"Your cards: {user_card} , current score: {curr_score}")
    print(f"Computer's first card: {comp_card[0]}")

    while not is_game_over:
        if curr_score == 0 or curr_comp_score == 0 or curr_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == 'y':
                user_card.append(deal_card())
                curr_score = calculate_score(user_card)
                print(f"Your cards: {user_card} , current score: {curr_score}")
                print(f"Computer's first card: {comp_card[0]}")
            else:
                is_game_over = True
                curr_score = calculate_score(user_card)
                curr_comp_score = calculate_score(comp_card)
            
    while curr_comp_score !=0 and curr_comp_score<17:
        comp_card.append(deal_card())
        curr_comp_score = calculate_score(comp_card)
            
    print(f"Your cards: {user_card} , current score: {curr_score}")
    print(f"Computer cards: {comp_card} , current score: {curr_comp_score}")
    print(compare(curr_score,curr_comp_score))     


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == 'y':  
    print_logo()
    play_game()