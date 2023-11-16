even_found = False
odd_found = False
first_even = 0
firs_odd = 0

while True:
    num = input("Enter an integer (or EXIT): ")
    if num == "EXIT":
        break
    num = int(num)

    if not even_found and num % 2 == 0:
        first_even = num
        even_found = True

    if not odd_found and num % 2 != 0:
        firs_odd = num
        odd_found = True

if not even_found:
    print("Even number not found")
else:
    print(f"First even number is {first_even}")
if not odd_found:
    print("Odd number not found")
else:
    print(f"First odd number is {firs_odd}")


