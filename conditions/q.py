

# n = 2100  #False
# n = 2024  #False
# n = 2000  #True
n = 2023    #True


ans = (n%4 and n%100!=0) or (n%100==0 and n%400 == 0)

print(ans)