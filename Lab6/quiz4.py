def next_number(number):
#{
    if (number%2 == 0):
        return 3 * number + 1
    else:
        return 2 * number + 2   
#}

# MAIN PROGRAM:

# ... type your code here ...
initial_num = int(input("Enter the initial number: "))
print("Sequence:")

counter = 0
while True:
    print(f"Step {counter}: {initial_num}")
    if initial_num > 100:
        break
    initial_num = next_number(initial_num)
    counter += 1

