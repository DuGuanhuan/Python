num_items = int(input("Enter the number of items: "))
print("\nReceipt:")
if num_items <= 50:
    print(f'{num_items} items x $3 = ${num_items * 3}')
    print('Postage: $10')
    print(f'Total: ${num_items * 3 + 10}')

else:
    print(f'{num_items} items x $2 = ${num_items * 2}')
    print('Postage: $0')
    print(f'Total: ${num_items * 2}')

