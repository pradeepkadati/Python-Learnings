import random
print(" Banker Roulette")

friends = ["Pradeep","Ram","Dhilip","Kandulapati"]
billPayer = friends[random.randint(0, len(friends)-1)]
print(f"{billPayer} is going to pay the bill")