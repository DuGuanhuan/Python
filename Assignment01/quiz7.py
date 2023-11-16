print("Laptop rental calculation")
laptop_brand = input("Enter the laptop brand: ")
application_cost = int(input("Enter the application cost: "))
monthly_cost = int(input("Enter the monthly cost: "))
num_months = int(input("Enter the number of months: "))

rental_cost = monthly_cost * num_months
total_cost = application_cost + rental_cost

print("\nRental cost for", laptop_brand, "laptop")
print(f"Application cost: ${application_cost}")
print(f"Rental cost: ${monthly_cost} x {num_months} month = ${rental_cost}")
print(f"Total cost: ${application_cost} + ${rental_cost} = ${total_cost}")
