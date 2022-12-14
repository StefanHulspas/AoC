f = open("Day1/input.txt", "r")
Lines = f.readlines()

elfCalories = []

cur = 0
for line in Lines:
    line = line.replace("\n", "")
    if not line:
        elfCalories.append(cur)
        cur = 0
    else:
        cur += int(line)

oneNum = 0
oneCal = 0
twoNum = 0
twoCal = 0
threeNum = 0
threeCal = 0

count = 0
for calories in elfCalories:
    if (calories > oneCal) :
        threeNum = twoNum
        threeCal = twoCal
        twoNum = oneNum
        twoCal = oneCal
        oneNum = count
        oneCal = calories
    elif (calories > twoCal):
        threeNum = twoNum
        threeCal = twoCal
        twoNum = count
        twoCal = calories
    elif (calories > threeCal):
        threeNum = count
        threeCal = calories
    count += 1


print("Elf1 {} has the most calories: {}".format(oneNum, oneCal))
print("Elf2 {} has the most calories: {}".format(twoNum, twoCal))
print("Elf3 {} has the most calories: {}".format(threeNum, threeCal))
print("Total: {}".format(oneCal + twoCal + threeCal))