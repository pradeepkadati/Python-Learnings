from wonderwords import RandomWord
import Hangman_art
print(Hangman_art.logo)
R_word_obj = RandomWord()
random_word = R_word_obj.word(word_max_length=5)
stage_count = 0
word_list = []
letter_found = False
user_won = False
for _ in range(len(random_word)):
    word_list.append("_")
#print(random_word)
while stage_count < len(Hangman_art.stages) and not user_won:
    guess_letter = input("Guess a letter:")
    letter_found = False
    for index in range(len(random_word)):
        word = random_word[index]
        if word == guess_letter:
            word_list[index] = guess_letter
            letter_found = True
    if not letter_found:
        stage_count += 1
    if (stage_count < len(Hangman_art.stages)) and ("_" not in word_list):
        user_won = True
    print(Hangman_art.stages[6 - stage_count])
    print(word_list)

if user_won:
    print("You win")
else:
    print("Oh may god, You are hanged")

