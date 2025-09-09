def factorial(a):
    ans = 1
    # for i in range(1,a+1):
    #     ans = ans*(i)
    i = 1
    while(i<=a):
        ans = ans*i
        i = i+1
    return ans

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
diff = (a-b)

factorialOfFirstNumber = factorial(a)
factorialOfSecondNumber = factorial(b)
factorialOfDifference = factorial(diff)

pnc = factorialOfFirstNumber//(factorialOfSecondNumber*factorialOfDifference)
print(pnc)