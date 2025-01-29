# ToDo 1 : Ask the user for input
# ToDo 2: Save data into dictionary {name: price}
# ToDo 3: Whether if new bids need to be added
# ToDo 4: Compare bids in dicionary
import os
def find_highest_bidder(bids):
    max_bid  = 0
    winner = " "
    for i in bids:
        bid_amount = bids[i]
        if(bid_amount>max_bid):
            max_bid=bid_amount
            winner = i
    print(f"The winner is {winner} with a bid of ${max_bid}")
    
    
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name? ")
    price = int(input("What is your bid?: $"))
    bids[name]=price
    should_continue = input("Are there any other bidders? Type 'yes or 'no' . \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes" :
        os.system('cls')
