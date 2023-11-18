numbers = []

while True:
    user_input = input("Enter an integer (enter QUIT to quit): ")

    if user_input == "QUIT":
        break

    number = int(user_input)
    numbers.append(number)

print("You have entered:", ', '.join(map(str, numbers)) + '.')

