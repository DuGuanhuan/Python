min_int = int(input("Min integer: "))
max_int = int(input("Max integer: "))

print("Display equation:")
for i in range(max_int, min_int - 1, -1):
    print(f"{i} + {i} + {i} = {i * 2} + {i} = {i * 3}")
