p = int(input("Enter the value of Principle: "))
r = int(input("Enter the value of Rate: "))
t = int(input("Enter time: "))

amount = p*(1+r/100)**t

si = (p*r*t)/100
ci = amount - p

print("Simple Interest:",si)
print("Compound Interest:",ci)