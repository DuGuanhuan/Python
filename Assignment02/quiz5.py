fruit_veg_cost: float = float(input("Enter the cost of Fruit&Veg: "))
deli_meals_cost = float(input("Enter the cost of Deli&Chilled Meals: "))
pantry_cost = float(input("Enter the cost of Pantry: "))

total_cost = fruit_veg_cost + deli_meals_cost + pantry_cost

use_mobile_discount = input("Would you like to use your 10% Woolworths Mobile discount? Y or N: ").strip().upper()
use_rewards_dollars = input("Would you like to use your $10 Everyday Rewards Dollars? Y or N: ").strip().upper()



print("\nReceipt:")
print(f"Fruit&Veg".ljust(45), f"{fruit_veg_cost:.2f}".rjust(9))
print(f"Deli&Chilled Meals".ljust(45), f"{deli_meals_cost:.2f}".rjust(9))
print(f"Pantry".ljust(45), f"{pantry_cost:.2f}".rjust(9))
print(f"Total".ljust(45), f"${total_cost:.2f}".rjust(9))    

if use_mobile_discount == 'Y':
    total_cost *= 0.9 
    saved_amount = (1 - 0.9) * (fruit_veg_cost + deli_meals_cost + pantry_cost)
    print(f"\n${saved_amount:.2f} saved with your Woolworths Mobile discount")
    print(f"Promotional Price".ljust(45),f"${total_cost:.2f}".rjust(9))

if use_rewards_dollars == 'Y':
    total_cost -= 10  
    print("\n$10 Everyday Rewards Dollars enjoyed")

print(f"\nPayment".ljust(45),f"${total_cost:.2f}".rjust(10))

# print("Payment                                         $104.53")