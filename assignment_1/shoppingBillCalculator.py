#Create a shopping bill calculator. Use variables for 3 items with their prices and quantities. Calculate subtotal, apply 10% tax, and display a detailed bill with f-strings.

item_1 = "Apple"; item_1_price = 20; item_1_quantity = 10
item_2 = "Bread"; item_2_price = 15; item_2_quantity = 22
item_3 = "Milk"; item_3_price = 65; item_3_quantity = 35

total_item_1 = item_1_price * item_1_quantity
total_item_2 = item_2_price * item_2_quantity
total_item_3 = item_3_price * item_3_quantity

subtotal = total_item_1 + total_item_2 + total_item_3

tax = subtotal * 0.10
total = subtotal + tax

print(f"{item_1}: {item_1_price} X {item_1_quantity} = {total_item_1}")
print(f"{item_2}: {item_2_price} X {item_2_quantity} = {total_item_2}")
print(f"{item_3}: {item_3_price} X {item_3_quantity} = {total_item_3}")
print(f"Subtotal: {subtotal}")
print(f"Tax (10%): {tax}")
print(f"Total: {total}")

