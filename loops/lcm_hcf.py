a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

#-----------------------HCF------------------------------#
# if a<b:
#     small = a
# else:
#     small = b

# for i in range(1,small+1):
#     if (a%i==0 and b%i==0):
#         hcf = i

# print(hcf)


#-----------------------LCM------------------------------#
if a>b:
    large = a
else:
    large = b

for i in range(large, a*b+1):
    if (i%a==0 and i%b==0):
        lcm = i
        break
print(lcm)