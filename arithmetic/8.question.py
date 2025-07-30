# days = 2000

days = int(input("Enter number of days: "))

year = days//365

# 5.479452
remaining_days = days - (year*365)

months = remaining_days//30

days = remaining_days - (months*30)

print(f"{year} year {months} months {days} days")