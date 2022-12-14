f = open("Day3/input.txt", "r")
Lines = f.readlines()

def mapPriority(char):
    num = ord(char)
    if num > ord('Z'):
        return num - ord('a') + 1
    else:
        return num - ord('A') + 27

lineTotal = len(Lines)
index = 0
score = 0

while index < lineTotal:
    firstElf = Lines[index]
    secondElf = Lines[index+1]
    thirdElf = Lines[index+2]
    found = False
    for charOne in firstElf:
        for charTwo in secondElf:
            if charOne == charTwo: 
                for charThree in thirdElf:
                    if (charOne == charThree):
                        found = True
                        score += mapPriority(charOne)
                        break
                if found:
                    break
        if found:
            break
    index += 3

print("Backpack score: {}".format(score))