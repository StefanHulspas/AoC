f = open("Day2/input.txt", "r")
Lines = f.readlines()

score = 0
for line in Lines:
    line = line.replace("\n", "")
    split = line.split(" ")
    target = ord(split[0])
    if split[1] == "X":
        target -= 1
    elif split[1] == "Y":
        score += 3
    elif split[1] == "Z":
        score += 6
        target += 1

    ordA = ord('A')
    ordB = ord('B')
    ordC = ord('C')

    if (target < ordA):
        target = ordC
    elif target > ordC:
        target = ordA
    
    if target == ordA:
        score += 1
    elif target == ordB:
        score += 2
    elif target == ordC:
        score += 3

print("Rock, Paper Scissor score: {}".format(score))