n = int(input("Enter number of lines: "))
numberOfSpaces = n//2
numberOfStars = 1

for lines in range(1,n+1):
    for i in range(1,numberOfSpaces+1):
        print(" ",end="")
    for j in range(1,numberOfStars+1):
        # print("*",end="")
        if j==1 or j==numberOfStars:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    if lines<=(n//2):
        numberOfSpaces = numberOfSpaces - 1
        numberOfStars = numberOfStars + 2
    else:
        numberOfSpaces = numberOfSpaces + 1
        numberOfStars = numberOfStars - 2