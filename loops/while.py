# max = 0

# i = 1
# while i<=5:
#     a = int(input(f"Enter number {i}"))
#     if a>max:
#         max = a
#     i = i+1

# print(max)


# a = int(input("Enter a number: "))
# temp = a
# reverse = 0

# while (a):
#     last = a%10
#     # print(last)
#     reverse = reverse*10 + last
#     a = a//10

# print(f"reverse of {temp} is {reverse}")

# if temp == reverse:
#     print("Palindrome")
# else:
#     print("Not Palindrome")





# a = int(input("Enter a Number: "))
# for i in range(a):
#     last = a%10
#     print(last)
#     a = a//10

#     if a==0:
#         break


a = int(input("Enter a number: "))
reverse = 0

while(a):
    last = a%10
    reverse = reverse*10 + last
    a = a//10

while(reverse):
    last = reverse%10
    print(last)
    reverse = reverse//10
