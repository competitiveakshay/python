n = int(input("Enter number of lines: "))

for lines in range(1,n+1):
    for i in range(1,(n-lines)+1):
        print(" ",end="")
    for i in range(1,(2*lines)):
        print("*",end="")
    print()