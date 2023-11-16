# Get user input
user_input = input("Enter a string: ")
case_choice = input("Uppercase or Lowercase? (U/L): ").strip().upper()

if case_choice == "U":
    result = user_input.upper()
    print(f"The Uppercase of {user_input} is {result}.")
elif case_choice == "L":
    result = user_input.lower()
    print(f"The Lowercase of {user_input} is {result}.")
else:
    print("Invalid input.")
