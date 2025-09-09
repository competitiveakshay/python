# a = "Rameshm"

# print(a.index("m"))
# print(a.rindex("m"))

a = "mamamamdddmaa"
s1 = ""

for ch in a:
    if (ch in s1) == False:
        s1 = s1 + ch
print(s1)