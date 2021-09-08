print("Welcome to Tip Calculator")
bill = input("What is the total Bill? $")
tip = input("what percentage would you like to give? 10,12 or 15")
split = input("How many people to split the bill?")

billAmt = float(bill)
tipAmt = (billAmt * int(tip)) / 100
billAmt += tipAmt

splitAmt = round((billAmt / int(split)), 2)
splitAmt = "{:.2f}".format(splitAmt)
print(f"Each person should pay: ${splitAmt}")




