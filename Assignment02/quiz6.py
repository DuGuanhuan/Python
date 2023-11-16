user_input = input("Which subject did you enroll in? (a) CSIT110 (b) CSIT881: ")
if user_input == 'a':
    print("You are an undergraduate.")
elif user_input == 'b':
    print("You are a postgraduate.")
else:
    print("Invalid input.")