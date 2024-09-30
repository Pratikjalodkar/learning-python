#make a auction system

from clear import clear

bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")



bidding_finish = False

while not bidding_finish:
    name = input("What`s your name: ")
    price = int(input("What`s your auction Bids: $"))
    bids[name] = price
    should_continue = input("Is there any other bids left type yes or no: ")
    if should_continue == "no":
        bidding_finish = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
        bidding_finish == False