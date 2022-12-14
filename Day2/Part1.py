f = open("Day2/input.txt", "r")
Lines = f.readlines()

score = 0
for line in Lines:
    line = line.replace("\n", "")
    split = line.split(" ")
    if split[1] == "X":
        split[1] = "A"
        score += 1
    elif split[1] == "Y":
        split[1] = "B"
        score += 2
    elif split[1] == "Z":
        split[1] = "C"
        score += 3

    diff = ord(split[0]) - ord(split[1])
    if diff == 0:
        score += 3
    elif diff == -1:
        score += 6
    elif diff == 2:
        score += 6

print("Rock, Paper Scissor score: {}".format(score))