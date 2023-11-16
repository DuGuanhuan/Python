# In a certain game, one of the objectives of the players is to collect tokens called "grassie" to purchase animals for their farm. The cost of one cow is 30 grassies, one duck is 5 grassies and one chick is 3 grassies. Study the example below carefully and write a program that works exactly like in the example:

# Enter number of cows to purchase: 1
# Enter number of ducks to purchase: 3
# Enter number of chicken to purchase: 4
# Cost:
# 1 cow = 30 grassies
# 3 duck = 15 grassies
# 4 chick = 12 grassies
# Total = 57 grassies

# Define the cost per animal
cost_per_cow = 30
cost_per_duck = 5
cost_per_chick = 3

# Input the number of animals to purchase
num_cows = int(input("Enter number of cows to purchase: "))
num_ducks = int(input("Enter number of ducks to purchase: "))
num_chickens = int(input("Enter number of chicken to purchase: "))

# Calculate the cost for each type of animal
total_cost_cows = num_cows * cost_per_cow
total_cost_ducks = num_ducks * cost_per_duck
total_cost_chickens = num_chickens * cost_per_chick

# Calculate the total cost
total_cost = total_cost_cows + total_cost_ducks + total_cost_chickens

# Display the cost breakdown and total
print("Cost:")
print(f"{num_cows} cow = {total_cost_cows} grassies")
print(f"{num_ducks} duck = {total_cost_ducks} grassies")
print(f"{num_chickens} chick = {total_cost_chickens} grassies")
print(f"Total = {total_cost} grassies")