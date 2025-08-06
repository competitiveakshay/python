# n = 2023

# if n%4==0:
#     print("May be a Leap Year")
#     if n%100!=0:
#         print("Leap Year")
#     elif n%100==0:
#         print("Century Year")
#         if n%400==0:
#             print("Leap Year")
#         else:
#             print("Not a leap year")
# else:
#     print("Not a leap year")

a = int(input("Enter a number: "))

if a%2==0:
    print("Even")
    if a%8==0:
        print("Div by 8")
    else:
        print("Not div by 8")
else:
    print("Odd")
    if a%5==0:
        print("Div by 5")
    else: 
        print("Not div by 5")