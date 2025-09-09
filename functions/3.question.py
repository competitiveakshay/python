# Take a number, find sum of square of its digits, plus sum of cubes of digits + sum of power of four of digits

# a = int(input("Enter a number: "))
# count = 0
# square = 0
# cube = 0
# four = 0
# finalSquare = 0
# finalFour = 0
# finalCube = 0

# while(a!=0):
#     last = a%10
#     square = last**2
#     finalSquare = finalSquare + square
#     cube = last**3
#     finalCube = finalCube + cube
#     four = last**4
#     finalFour = finalFour + four
#     a = a//10

# ans = finalFour + finalCube + finalSquare
# print(ans)

a = int(input("Enter a number: "))

def sumOfPower(n,p):
    sum = 0
    while n>0:
        last = n%10
        sum = sum + last**p
        n = n//10
    return sum

ans = sumOfPower(a,2) + sumOfPower(a,3) + sumOfPower(a,4)
print(ans)
