# small = int(input("Enter first number: "))

# for i in range(4):
#     a = int(input(f"Enter number {i+2}: "))
#     if a<small:
#         small = a

# print(small)



small = int(input("Enter first number: "))
second_smallest = small

for i in range(4):
    a = int(input(f"Enter number {i+2}: "))
    if a<small:
        second_smallest = small
        small = a
    elif a<second_smallest and a!=small:
        second_smallest = a

print(second_smallest)