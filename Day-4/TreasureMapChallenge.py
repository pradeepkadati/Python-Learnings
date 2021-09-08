print(" Treasure Map Challenge")

row1 = ["-", "-", "-"]
row2 = ["-", "-", "-"]
row3 = ["-", "-", "-"]

map = [row1, row2, row3]

position = input("Where do you want to please the treasure:")

col = int(position[0])
row = int(position[1])

map[row-1][col-1] = "X"

print(f"{map[0]}\n{map[1]}\n{map[2]}")
