n = int(input("Enter number of lines: "))

for lines in range(1,n+1):
    for i in range(n-lines+1):
        print(" ",end="")
    for i in range(lines+1):
        print("*")
    print()
    