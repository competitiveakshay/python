#------------------------------------------------------------------#
# Q1 Take a number and check if it is div by 2 or not.

# a = int(input("Enter a number: "))

# if (a%2==0):
#     print(f"{a} is divisible by 2")
# else:
#     print(f"{a} is not divisible by 2")
#------------------------------------------------------------------#

#------------------------------------------------------------------#
# Q2 Take a number and check if it is integer number or decimal number

# a = float(input("Enter a number: "))
# integet_a = int(a)
# decimal_part = a - integet_a

# if(decimal_part == 0):
#     print(f"{a} is integer")
# else:
#     print(f"{a} is decimal")
#------------------------------------------------------------------#

#-------------------------------------------------------------#
# Q3 Take two numbers and print the biggest number

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if(a>b):
#     print(a)
# elif(b>a):
#     print(b)

#--------------------------------------------------------------#

#--------------------------------------------------------------#
# Q4 Take three number and print the biggest number

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if(a>b and a>c):
#     print(a)
# elif(b>a and b>c):
#     print(b)
# elif(c>a and c>b):
#     print(c)

#--------------------------------------------------------------#

#--------------------------------------------------------------#
# Q5 Take a  number and check it is 1 digit number, or 2 digit number, or 3 digit number or something else.


# a = int(input("Enter a number: "))

# if(a>0 and a<10):
#     print(f"{a} is 1 digit number")
# elif(a>=10 and a<100):
#     print(f"{a} is 2 digit number")
# elif(a>=100 and a<1000):
#     print(f"{a} is 3 digit number")
# else:
#     print(f"{a} is something else")


# if(a>0 and a<10):
#     print(f"{a} is 1 digit number")
# elif a<100:
#     print(f"{a} is 2 digit number")
# elif a<1000:
#     print(f"{a} is 3 digit number")
# else:
#     print(f"{a} is something else")

#-----------------------------------------------------#

#-----------------------------------------------------#

# convert 24 hrs time format to 12 hrs time format

# hr = int(input("Enter hour: "))
# min = int(input("Enter minutes: "))
# sec = int(input("Enter seconds: "))

# if hr>12 and hr<24:
#     new_hr = hr-12
#     print(f"{new_hr} hrs {min} minutes {sec} seconds")
# elif hr==12:
#     print(f"{hr} hrs {min} minutes {sec} seconds")
# elif hr==24:
#     print(f"00 hrs {min} minutes {sec} seconds")
# else:
#     print(f"{hr} hrs {min} minutes {sec} seconds")


# if hr==0:
#     print(f"{12}:{min}:{sec} AM")
# elif hr<12:
#     print(f"{hr}:{min}:{sec} AM")
# elif hr>12:
#     print(f"{hr-12}:{min}:{sec} PM")
# elif hr==12:
#     print(f"{hr}:{min}:{sec} PM")

#-----------------------------------------------------#

#-----------------------------------------------------#

a = 36
b = 72
c = 72

if a==b and c==a:
    print("ISOSCELES")
else:
    print("Not Isosceles")