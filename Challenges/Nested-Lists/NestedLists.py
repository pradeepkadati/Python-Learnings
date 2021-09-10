students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

scores = []
second_min_score = 0
for student in students:
    scores.append(student[1])
scores.sort()
for i in range(len(scores)-1):
    if scores[i+1] > scores[i]:
        second_min_score = scores[i + 1]
        break
names = []
for student in students:
    if student[1] == second_min_score:
        names.append(student[0])
names.sort()
for name in names:
    print(name)




