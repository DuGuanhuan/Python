String = input("Enter a string: ")
char_perline = int(input("Enter a positive integer: "))

print("Display pattern: ")

for i in String:
    print(i * char_perline)