import random

score = random.randint(1,100)

with open("highscore.txt") as f:
    highscore = f.read()
    if highscore == "":
        highscore = 0
    else:
        highscore = int(highscore)


if score>highscore:
    with open("highscore.txt", "w") as f:
        f.write(str(score))

print(score)