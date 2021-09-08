from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def find_bid_winner(bids):
    max_bid_amt = 0
    bid_winner = {}
    for key in bids:
        if bids[key] > max_bid_amt:
            bid_winner.clear()
            bid_winner[key] = bids[key]
    print(f" Bid winner is {bid_winner}")


bidders = {}
bidder_name = input("Enter your name:")
bidder_quote = int(input("Enter Bid quote amount:"))

bidders[bidder_name] = bidder_quote

more_bidders = input("Are there more bidders:")

while more_bidders == "yes":
    clear()
    bidder_name = input("Enter your name:")
    bidder_quote = int(input("Enter Bid quote amount:"))
    bidders[bidder_name] = bidder_quote
    more_bidders = input("Are there more bidders:")

find_bid_winner(bidders)

