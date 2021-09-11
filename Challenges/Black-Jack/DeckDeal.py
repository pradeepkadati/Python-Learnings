import random
import Cards
from typing import List

card_deals = []


def deal_deck(times):
    card_deals.clear()
    for i in range(times):
        random_index = random.randint(0, len(Cards.cards_deck)-1)
        card_deals.append(Cards.cards_deck[random_index])
    return card_deals


def deal_score(deals: List[int], final):
    total_deal = 0

    if final:
        total_deal = sum(deals)
        while total_deal <= 16:
            final_deal = deal_deck(1)[0]
            deals.append(final_deal)
            total_deal += final_deal

    else:
        total_deal = sum(deals)
        if deals.__contains__(11):
            if total_deal > 21:
                total_deal -= 10

    return total_deal


