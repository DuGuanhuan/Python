n = int(input("Enter a positive integer: "))

# Determine the number of spaces needed for formatting
num_spaces = n - 1

for i in range(1, n + 1):
    print(" " * num_spaces * 2, end="")
    
    # Print increasing numbers
    for j in range(1, i):
        print(j, end=" ")
    
    # Print decreasing numbers
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    # Move to the next line
    print()
    
    # Decrease the number of spaces
    num_spaces -= 1
