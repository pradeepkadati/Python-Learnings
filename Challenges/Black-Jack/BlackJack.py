import DeckDeal
print("Welcome to Black Jack")

start_deal = input("Would you like to play black jack? Press 'y' to play:")
dealer_deals = []
player_deals = []
if start_deal == "y":
    dealer_deals.extend(DeckDeal.deal_deck(2))
    player_deals.extend(DeckDeal.deal_deck(2))


print(f"Dealer Deals are [{dealer_deals[0]},x] -> {dealer_deals[0]}")
print(f"Player Deals are {player_deals} -> {DeckDeal.deal_score(player_deals, False)} ")

more_deal = input("Would you like to have another deal? Press 'y' another deal else Press 'n':")
dealer_score = 0
player_score = 0
while more_deal == "y":
    player_deals.extend(DeckDeal.deal_deck(1))
    dealer_score = DeckDeal.deal_score(dealer_deals, False)
    player_score = DeckDeal.deal_score(player_deals, False)
    if dealer_score == 21 and player_score == 21:
        print("Game Drew")
        print(f"Dealer Deals are {dealer_deals} -> {dealer_score}")
        print(f"Player Deals are {player_deals} -> {player_score} ")
        break
    elif dealer_score > 21:
        print("Player Wins")
        print(f"Dealer Deals are {dealer_deals} -> {dealer_score}")
        print(f"Player Deals are {player_deals} -> {player_score} ")
        break
    elif player_score > 21:
        print("Dealer wins")
        print(f"Dealer Deals are {dealer_deals} -> {dealer_score}")
        print(f"Player Deals are {player_deals} -> {player_score} ")
        break
    else:
        print(f"Dealer Deals are [{dealer_deals[0]},x] -> {dealer_deals[0]}")
        print(f"Player Deals are {player_deals} -> {DeckDeal.deal_score(player_deals, False)} ")
        more_deal = input("Would you like to have another deal? Press 'y' another deal else Press 'n':")

if more_deal == "n":
    dealer_score = DeckDeal.deal_score(dealer_deals, True)
    player_score = DeckDeal.deal_score(player_deals, False)
    if dealer_score == player_score:
        print("Game Drew")
        print(f"Dealer Deals are {dealer_deals} -> {dealer_score}")
        print(f"Player Deals are {player_deals} -> {player_score} ")
    elif player_score < dealer_score <= 21:
        print("Dealer Wins")
        print(f"Dealer Deals are {dealer_deals} -> {dealer_score}")
        print(f"Player Deals are {player_deals} -> {player_score} ")
    else:
        print("Player Wins")
        print(f"Dealer Deals are {dealer_deals} -> {dealer_score}")
        print(f"Player Deals are {player_deals} -> {player_score} ")


