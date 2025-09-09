a = input("Enter a string: ")
# k = int(input("Enter number of substr: "))

for lines in range(0,len(a)):
    for i in range(lines,len(a)):
        print(a[i],end=",")
    print()

# for i in range(0,len(a)-k+1):
#     print(a[i:i+k])
    

# print(a[-4:-1])
# print(a[1:-1])
# print(a[1:5:2])
# print(a[-2:-5:-1])
# print(a[-1::-1])
# print(a[::])

