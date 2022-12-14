f = open("Day3/input.txt", "r")
Lines = f.readlines()

def mapPriority(char):
    num = ord(char)
    if num > ord('Z'):
        return num - ord('a') + 1
    else:
        return num - ord('A') + 27

score = 0
for line in Lines:
    line = line.replace("\n", "")
    length = len(line)
    one = line[0:length//2]
    two = line[length//2: length]
    found = False
    for charOne in one:
        for charTwo in two:
            if charOne == charTwo: 
                found = True
                val = mapPriority(charOne)
                score += val
                break
        if found:
            break

print("Backpack score: {}".format(score))