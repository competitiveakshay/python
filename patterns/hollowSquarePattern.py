

for row in range(1,5):
  if row == 1 or row == 4:
    for i in range(1,5):
      print("* ",end=" ")
  else:
    print("*",end="")
    for i in range(1,4):
      print("  ",end="")
    print("*",end="")
  print()