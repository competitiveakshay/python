# Take a string print only those characters which are at even position
# a = input("Enter a string: ")

# for ch in range(len(a)):
#     if ch%2==0:
#         print(a[ch])
#---------------------------------------------------------------#

#---------------------------------------------------------------#
# Take a string and print it in reverse order

a = input("Enter a string: ")
# for ch in range(len(a)-1,-1,-1):
#     print(a[ch])
# print()
# print()
# print()
# for i in range(-1, -len(a)-1, -1):
#     print(i,a[i])

rev = ""

# for i in range(len(a)-1,-1,-1):
#     rev = rev + a[i]
# print(rev)

for ch in a:
    rev = ch + rev
print(rev)

#---------------------------------------------------------------#

#---------------------------------------------------------------#

# Take a number and find sum of its digits using string concepts.

# n = int(input("Enter a number: "))
# s = str(n)
# sum = 0
# for ch in s:
#     sum = sum + int(ch)
# print(f"sum of digits of {n} is {sum}")

#---------------------------------------------------------------#

#---------------------------------------------------------------#

# printing only vowels

# a = input("Enter a string: ")
# for i in a:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
#         print(i)

#------------------------------------------------------------------#

#------------------------------------------------------------------#

# str = "AKshay"

# print("a" in str)
# print("z" in str)

#------------------------------------------------------------------#
    