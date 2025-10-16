import pandas as pd


# print(pd.__version__)

# data = {
#     "Name": ["Noida", "Delhi", "Gujrat"],
#     "Age": [21,22,23]
# }

# df = pd.DataFrame(data)
# print(df)

car_data = {
    "Car_Name": ["M-alto", "Scorpio-N"],
    "Model_number": [12345, 67890]
}

df = pd.DataFrame(car_data)
# print(df)
df.to_csv("car.csv", index=False)
df.to_excel("car.xlsx", index=False)  
df.to_json("car.json")
print(df)