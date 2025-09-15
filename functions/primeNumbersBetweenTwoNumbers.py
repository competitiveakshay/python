a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a>b:
    large = a
    small = b
else:
    large = b
    small = a

def checkPrime(n):
    count = 0
    for i in range(1,n+1):
        if (n%i)==0:
            count = count + 1
    if count == 2:
        return True

    return False

for i in range(small,large+1):
    if checkPrime(i) == True:
        print(i)