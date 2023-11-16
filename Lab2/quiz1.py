product_code = input("Enter product code: ")# ABC123
product_name = input("Enter product name: ")# Green eggs and ham
product_size = input("Enter product size: ")#300mg
product_price = float(input("Enter product price: ")) #2.5

print(f"{product_code}: {product_name}, {product_size}")
print(f"{product_name}, {product_size}, ${product_price:.2f}")
print(f'{product_code}: "{product_name}"')
