print("Average Student height")

stu_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0

for height in stu_heights:
    total_height += height

print(f" Avg height is {round(total_height/len(stu_heights))}")