n = int(input("Enter a number: "))

def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)

if n<0:
    print("Invalid Number")
else:
    ans = fact(n)

print(ans)