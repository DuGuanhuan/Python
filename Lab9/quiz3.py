def generate_fibonacci(n):
    fibonacci_list = [0, 1]

    for _ in range(2, n):
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)

    return fibonacci_list[:n]


num_item = int(input("How many Fibonacci numbers to generate? "))

print(f"Here is a list of generated Fibonacci numbers: {generate_fibonacci(num_item)}")