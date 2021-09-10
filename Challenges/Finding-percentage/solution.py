student_marks = {"Krishna":[67, 68, 69,],
                 "Arjun":[70, 98, 63],
                 "Malika":[52, 56, 60]}
query_name = "Malika"

scores = student_marks[query_name]

print(round(sum(scores)/len(scores),2))