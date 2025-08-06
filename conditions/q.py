

# n = 2100  
# n = 2024  
n = 2000  
# n = 2023    


ans = (n%4==0 and n%100!=0) or (n%100==0 and n%400 == 0)

print(ans)