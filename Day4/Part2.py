f = open("Day4/input.txt", "r")
Lines = f.readlines()

def contains(first,second):
    firstSplit = first.split('-')
    secondSplit = second.split('-') 
    if int(firstSplit[0]) <= int(secondSplit[0]) and int(firstSplit[1]) >= int(secondSplit[0]):
        return True
    elif int(firstSplit[0]) <= int(secondSplit[1]) and int(firstSplit[1]) >= int(secondSplit[1]):
        return True
    return False

score = 0
for line in Lines:
    line = line.replace("\n", "")
    split = line.split(',')
    if contains(split[0], split[1]):
        score += 1
    elif contains(split[1], split[0]):
        score += 1

print("Sections score: {}".format(score))