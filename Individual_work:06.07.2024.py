filename = '/content/prices.txt'

total_price_of_all_items = 0.0
total_number_of_purchased_items = 0

with open(filename, 'r') as file:
    for line in file:
        try:
            price = float(line)
            total_price_of_all_items += price
            total_number_of_purchased_items += 1
        except ValueError:
            continue

print(f"Total price of all items: {total_price_of_all_items:.2f} €")
print(f"Total number of purchased items: {total_number_of_purchased_items}")
