print("Treasue Island")

left_right = input("Would you like to go left or right:")

if left_right == "left":
    print("Going Left...")
    swim_wait = input("Would you like to swim or wait for boat:")
    if swim_wait == "wait":
        print("Waiting for boat...")
        door = input("which door would you like to open. Red,Blue or Yellow:")
        if door == "blue":
            print("Congrats, You won the game")
        else:
            print("GAME OVER")
    else:
        print("GAME OVER")
else:
    print("GAME OVER")
