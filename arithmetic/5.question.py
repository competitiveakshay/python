a = int(input("Enter a three digit number: "))

last_digit = a%10
first_digit = (a - last_digit)//10
# print("First digit: ",first_digit)
# print("Last digit: ",last_digit)

reverse_digit = last_digit*10 + first_digit
# print(reverse_digit)
print(f"{last_digit}{first_digit}")