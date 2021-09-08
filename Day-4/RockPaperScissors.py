import random
print("Welcome to Rock Paper Scissor")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_img = [rock, paper, scissors]

user_sel = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissor:"))
sys_sel = random.randint(0, 2)
print(f"user selected \n {game_img[user_sel]}")
print(f"Computer selected \n {game_img[sys_sel]}")
if user_sel == 0:
    if sys_sel == 1:
        print(" Computer Wins")
    elif sys_sel == 2:
        print(" You Wins")
    else:
        print("You drew")
elif user_sel == 2:
    if sys_sel == 0:
        print(" Computer Wins")
    elif sys_sel == 1:
        print(" You Wins")
    else:
        print("You drew")
else:
    if sys_sel == 2:
        print(" Computer Wins")
    elif sys_sel == 1:
        print(" You Wins")
    else:
        print("You drew")
