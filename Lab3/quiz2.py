def calculate_cost(num_items):
    if num_items <= 50:
        item_cost = num_items * 3
    else:
        item_cost = num_items * 2
    return item_cost


def calculate_postage(num_items, shipping_method):
    if shipping_method == "s":
        postage_cost = 10 if num_items <= 50 else 0
    elif shipping_method == "r":
        postage_cost = 15 if num_items <= 50 else 10
    elif shipping_method == "e":
        postage_cost = 20 if num_items <= 50 else 17
    else:
        print("Invalid shipping method. Please enter 's', 'r', or 'e'.")
        exit()
    return postage_cost

# Input the number of items and shipping method
num_items = int(input("Enter the number of items: "))
shipping_method = input("Enter shipping method (s/r/e): ")

# Calculate the item cost and postage cost
item_cost = calculate_cost(num_items)
postage_cost = calculate_postage(num_items, shipping_method)

# Calculate the total cost
total_cost = item_cost + postage_cost

# Display the receipt
print("\nReceipt:")
if num_items <= 50:
    print(f'{num_items} items x $3 = ${num_items * 3}')
    if shipping_method == "s":
        print(f'Standard post: ${postage_cost}')
    elif shipping_method == "r":
        print(f'Registered post: ${postage_cost}')
    elif shipping_method == "e":
        print(f'Express post: ${postage_cost}')
    print(f'Total: ${total_cost}')

else:
    print(f'{num_items} items x $2 = ${num_items * 2}')
    if shipping_method == "s":
        print(f'Standard post: ${postage_cost}')
    elif shipping_method == "r":
        print(f'Registered post: ${postage_cost}')
    elif shipping_method == "e":
        print(f'Express post: ${postage_cost}')
    print(f'Total: ${total_cost}')
