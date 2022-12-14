f = open("Day1/input.txt", "r")
Lines = f.readlines()

elfCalories = []

cur = 0
for line in Lines:
    line = line.replace("\n", "")
    if not line:
        elfCalories.append(cur)
        print("Line{}: {}".format(elfCalories.__len__, cur))
        cur = 0
    else:
        cur += int(line)

maxCalories = elfCalories[0]
elfNum = 0

count = 0
for calories in elfCalories:
    if (calories > maxCalories) :
        maxCalories = calories
        elfNum = count
    count += 1


print("Elf{} has the most calories: {}".format(elfNum, maxCalories))