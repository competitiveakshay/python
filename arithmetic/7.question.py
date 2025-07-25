a = int(input("Enter a three digit number: "))

last_digit = a%10
last_two_digit = a//10
mid_digit = last_two_digit%10
# first_digit = (last_two_digit - mid_digit)//10
first_digit = last_two_digit//10

reverse_number = last_digit*100 + mid_digit*10 + first_digit

print(first_digit)
print(mid_digit)
print(last_digit)
print(reverse_number)