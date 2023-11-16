while True:
    num = input("Enter an integer (or exit): ")
    if num.lower() == 'exit':
        break
    num = int(num)

    if num > 0:
        print(f"Positive integer, display addition: {num} + {num} = {num + num}")
    elif num < 0:
        print(f"Negative integer, display multiplication: ({num}) x ({num}) = {num * num}")
    else:
        print("Zero, display just zero: 0")
