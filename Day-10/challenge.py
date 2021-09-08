n = int(input("N"))
arr = map(int, input("array").split())
scores = list(arr)
print(max(scores))
scores.sort(reverse=True)
print(scores)
print(sorted(list(set(scores)))[-2])
for i in range(len(scores)):
    if scores[i] > scores[i+1]:
        print(scores[i+1])
        break

