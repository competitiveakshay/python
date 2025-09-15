n = int(input("Enter number of lines: "))
numberOfStars = 1
numberOfSpaces = n//2

for lines in range(1,n+1):
    for i in range(1,numberOfSpaces+1):
        print(" ",end="")
    for i in range(1,numberOfStars+1):
        print("*",end="")
    print()
    if lines<5:
        numberOfStars = numberOfStars + 2
        numberOfSpaces = numberOfSpaces - 1
    else:
        numberOfStars = numberOfStars - 2
        numberOfSpaces = numberOfSpaces + 1