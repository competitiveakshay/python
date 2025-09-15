

# for row in range(1,5):
#   if row == 1 or row == 4:
#     for i in range(1,5):
#       print("* ",end=" ")
#   else:
#     print("*",end="")
#     for i in range(1,4):
#       print("  ",end="")
#     print("*",end="")
#   print()

for row in range(1,5):
    for col in range(1,5):
        if row==1 or row==4 or col==1 or col==4:
            print("*",end=" ")
        else:
            print("  ",end="")
    print()
    