print("Love Calculator")

name1 = input("Enter your name:")
name2 = input("Enter your Love name:")

combined_name = name1.lower()+name2.lower()

true_count = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")

love_count = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")

tl_count = (true_count * 10) + love_count

if tl_count < 10 or tl_count > 90:
    print(f" your score is {tl_count}, you go together like coke and mentos")
elif 40 < tl_count < 50:
    print(f" your score is {tl_count}, you are alright together")
else:
    print(f" your score is {tl_count}")